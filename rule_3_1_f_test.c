/* flag ? 10 : 20	Don't check */
// flag ? 10 : 20	Don't check
a = (flag ? 10 : 20); // flag?10:20

a = (flag ? x = 40 : 20); // flag?10:20

a = /* flag ? 10 : 20 Don't check */ flag?0:1; // Error

/*
	Don't check

 	a = flag?  0:     1
 */
a = flag            ?  0:               1  ; // Error

x = "(flag ? 10 : 20)"; // Don't check

a = flag ? flag ? 3 :5 :9; // Error

a = flag ? flag ? 3 : 5 : 9; // OK

a = flag ? 5 : flag ? 2 : 2; // OK

a = flag ?5 :flag ? 2 : 2; // Error

a = flag ? 1 : 2 ? 2 : 3; // OK

a = flag ? 1 :2 ?2 : 3;  // Error

a = flag                   ?                     1            :                3           ;  // Error

a = flag ? flag ? 10 : 20 ? 3 : 5 : 9; // OK

x = "a = flag            ?  0:               1 "; // Don't check

switch(5)
{
	case 1: // Don't check
		break;
	case 2: // Don't check
		break;
}