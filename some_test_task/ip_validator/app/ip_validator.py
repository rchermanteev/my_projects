from prettytable import PrettyTable
from cmd import Cmd
if 64 - 64: i11iIiiIii
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
o0OO00 = ord ( '0' )
oo = 7
i1iII1IiiIiI1 = chr
iIiiiI1IiI1I1 = "Wrong"
o0OoOoOO00 = i1iII1IiiIiI1 ( 46 )
I11i = i1iII1IiiIiI1 ( 58 )
if 64 - 64: OOooo000oo0 . i1 * ii1IiI1i % IIIiiIIii
if 8 - 8: Oo / iII11iiIII111 % iiiIIii1I1Ii . O00oOoOoO0o0O
class Validate:
 def __init__ ( self ) :
  self . items = "1234567890abcdefgABCDEFG"
  self . table = PrettyTable ( [ "IP" , "Verdict" ] )
  self . db = [ ]
  if 16 - 16: Iii1iIIIII . II1i * o00ooo0 / o00 * O0IiiiIiI1iIiI1 - ooo0Oo0
 def validateIPAddress ( self , ips ) :
  for ooO0Oooo00 in ips :
   if ooO0Oooo00 . count ( o0OoOoOO00 ) == ( int ( i1iII1IiiIiI1 ( o0OO00 ) ) + 1 ) * 3 :
    Ooo0 = self . validateone ( ooO0Oooo00 )
   elif ooO0Oooo00 . count ( I11i ) == ( int ( i1iII1IiiIiI1 ( o0OO00 ) ) + 1 ) * 7 or ooO0Oooo00 . count ( o0OoOoOO00 ) == ( int ( chr ( o0OO00 ) ) + 1 ) * 4 :
    if ooO0Oooo00 == ( i1iII1IiiIiI1 ( o0OO00 ) + I11i ) * 7 + i1iII1IiiIiI1 ( o0OO00 + 1 ) :
     Ooo0 = iIiiiI1IiI1I1
    else :
     Ooo0 = self . validatetwo ( ooO0Oooo00 )
   elif ooO0Oooo00 . count ( I11i ) == oo :
    Ooo0 = self . validatetwo ( ooO0Oooo00 )
   else :
    Ooo0 = iIiiiI1IiI1I1
   self . db . append ( [ ooO0Oooo00 , Ooo0 ] )
   self . table . add_row ( [ ooO0Oooo00 , Ooo0 ] )
  print ( self . table )
  self . table . clear_rows ( )
  return self . db
  if 89 - 89: I111i1i1111i - iIii1I11I1II1 % O0IiiiIiI1iIiI1
 def validateone ( self , ip ) :
  for oOo0oooo00o in ip . split ( o0OoOoOO00 ) :
   if not oOo0oooo00o . isdigit ( ) or str ( int ( oOo0oooo00o ) ) != oOo0oooo00o or int ( oOo0oooo00o ) > 254 or int ( oOo0oooo00o ) < 0 :
    return iIiiiI1IiI1I1 + " IPv4"
  return "Valid IPv4"
  if 65 - 65: iII11iiIII111 * iIii1I11I1II1 * I111i1i1111i
 def validatetwo ( self , ip ) :
  for oOo0oooo00o in ip . split ( I11i ) :
   if not oOo0oooo00o or not oOo0oooo00o . isalnum ( ) or len ( oOo0oooo00o ) > 4 or any ( char not in self . items for char in oOo0oooo00o ) :
    if 18 - 18: iIii1I11I1II1 / II1i + O00oOoOoO0o0O / ii1IiI1i - OOooo000oo0 - II1i
    return iIiiiI1IiI1I1 + " IPv6"
  return "Valid IPv6"
  if 1 - 1: II1i - Iii1iIIIII % O0 + i1 - o00 / II1i
  if 31 - 31: IIIiiIIii + OOooo000oo0
  if 13 - 13: Iii1iIIIII * O00oOoOoO0o0O * i1
class oOOOO ( Cmd ) :
 validator = Validate ( )
 if 45 - 45: ooo0Oo0 + o00ooo0
 def do_validate ( self , args ) :
  args = args . split ( ' ' )
  if len ( args ) == 0 :
   print ( "Provide your IPs" )
  else :
   self . validator . validateIPAddress ( args )
   if 17 - 17: iII11iiIII111
def o00ooooO0oO ( ) :
 oOoOo00oOo = oOOOO ( )
 oOoOo00oOo . prompt = '> '
 oOoOo00oOo . cmdloop ( 'Start IP validator...' )
 if 96 - 96: i1IIi . Oo * Iii1iIIIII % I111i1i1111i
if __name__ == '__main__' :
 o00ooooO0oO ( )
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
