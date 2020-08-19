#include <iostream>
#include <vector>
#include <iomanip>
#include <conio.h>
#include <windows.h>
#include <ctime>


using namespace std;

# define B_UP 230
# define B_DOWN 235
# define B_LEFT 228
# define B_RIGHT 162
# define B_ESC 27

int game_score = 0;

bool game_run = true;

bool is_loot = false;


void clearKeyboardBuffer()
{
	while (_kbhit())
	{
		_getch();
		break;
	}
}


void printField(vector<vector<int>> &field) {

	for (vector<vector<int>>::iterator y = field.begin(); y != field.end(); ++y) {
		cout << endl;
		for (vector<int>::iterator x = (*y).begin(); x != (*y).end(); ++x) {
			switch (*x) {
			case 0:
				cout << setw(2) << "";
				break;

			case -1:
				cout << setw(2) << "#";
				break;

			case 1:
				cout << setw(2) << "o";
				break;

			case 2:
				cout << setw(2) << "O";
				break;

			case 10:
				cout << setw(2) << "F";
				break;
			}
		}
	}

	cout << "\nScore: " << game_score << endl;

}


void setUp(vector<vector<int>> &field, int &size_field, pair<int, int> &p_head_snake, vector<pair<int, int>>& snake_body) {

	for (int i{ 0 }; i < size_field; i++) {
		field[0][i] = -1;
		field[size_field - 1][i] = -1;
		field[i][0] = -1;
		field[i][size_field - 1] = -1;
	}

	srand(time(NULL));

	p_head_snake = { 1 + rand() % (size_field - 2), 1 + rand() % (size_field - 2) };

	snake_body.push_back(p_head_snake);

	field[p_head_snake.first][p_head_snake.second] = 2;

}


int execute(pair<int,int> &p_head_snake) {

	//field[p_head_snake.first][p_head_snake.second] = 0;

	while (_kbhit()) {

		int a = _getch();
		cout << a << endl;

		switch (a) {
		case B_UP:
			p_head_snake.first -= 1;
			return B_UP;

		case B_DOWN:
			p_head_snake.first += 1;
			return B_DOWN;

		case B_LEFT:
			p_head_snake.second -= 1;
			return B_LEFT;

		case B_RIGHT:
			p_head_snake.second += 1;
			return B_RIGHT;

		case B_ESC:
			game_run = false;
			return 0;

		default:
			break;
		}

		return 0;
	}
}

void turn_whithout_user_action(pair<int, int>& p_head_snake, int prev_action) {
	switch (prev_action) {
	case B_UP:
		p_head_snake.first -= 1;
		break;

	case B_DOWN:
		p_head_snake.first += 1;
		break;

	case B_LEFT:
		p_head_snake.second -= 1;
		break;

	case B_RIGHT:
		p_head_snake.second += 1;
		break;

	case B_ESC:
		game_run = false;
		break;

	default:
		break;
	}
}


void generate_loot(vector<vector<int>>& field, int& size_field) {
	srand(time(NULL));

	pair<int, int> p_loot;

	while (!is_loot) {
		p_loot = { 1 + rand() % (size_field - 2), 1 + rand() % (size_field - 2) };

		if (field[p_loot.first][p_loot.second] == 0) {
			field[p_loot.first][p_loot.second] = 10;
			is_loot = true;
		}
	}	
}

void incrise_snake_body(vector<pair<int, int>>& snake_body, pair<int, int>& snake_head) {
	snake_body.push_back(snake_head);
}

void move_snake_body(vector<pair<int, int>>& snake_body, pair<int, int>& snake_head) {
	for (vector<pair<int, int>>::iterator it = snake_body.begin(); it != (snake_body.end() - 1) ; it++) {
		*(it) = *(it + 1);
	}
	snake_body[size(snake_body) - 1] = snake_head;
}


void logic(vector<vector<int>>& field, int& size_field, pair<int, int>& p_head_snake, vector<pair<int, int>>& snake_body) {


	//field[snake_body[0].first][snake_body[0].second] = 0;


	switch (field[p_head_snake.first][p_head_snake.second]) {
	case -1:
		game_run = false;
		break;

	case 0:
		//field[p_head_snake.first][p_head_snake.second] = 1;
		field[snake_body[0].first][snake_body[0].second] = 0;
		move_snake_body(snake_body, p_head_snake);
		break;

	case 1:

		game_run = false;
		break;

	case 10:
		field[p_head_snake.first][p_head_snake.second] = 0;
		field[snake_body[0].first][snake_body[0].second] = 0;
		incrise_snake_body(snake_body, p_head_snake);
		is_loot = false;
		game_score += 10;
		break;

	default:
		break;
	}

	for (vector<pair<int, int>>::iterator it = snake_body.begin(); it != snake_body.end(); ++it) {
		field[(*it).first][(*it).second] = 1;
	}
	field[snake_body[size(snake_body) - 1].first][snake_body[size(snake_body) - 1].second] = 2;

}


int main() {

	int size_field = 15;
	vector<vector<int>> field(size_field, vector<int>(size_field, 0));;
	pair<int, int> p_head_snake;
	vector<pair<int, int>> snake_body;
	

	setUp(field, size_field, p_head_snake, snake_body);

	int user_action = 0;
	int prev_user_action = -1;

	while (game_run) {
		printField(field);
		
		user_action = execute(p_head_snake);

		cout << user_action << endl;
		cout << prev_user_action << endl;

		if (user_action)
			prev_user_action = user_action;

		if (!user_action) {
			turn_whithout_user_action(p_head_snake, prev_user_action);
		}

		logic(field, size_field, p_head_snake, snake_body);
		generate_loot(field, size_field);
		
		clearKeyboardBuffer();
		

		Sleep(1000/2);
		system("cls");
		
	}
	
		
	return 0;
}