if () {print();} // Error
else if () {print();} // Error
else {print(); print(); print();} // Error
print(); print(); // Error

print(); // OK

if () { // OK
    print(); // OK
} else { if () {print();} // Error
}

while () {print();} // Error

for () {print();} // Error

while () {} // OK

for () { // OK
}

/* Don't check

if () {print();}
else if () {print();}
else {print(); print(); print();}
print(); print();

print();

if () {
    print();
}

while () {print();}


*/
