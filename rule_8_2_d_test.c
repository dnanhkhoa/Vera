if () // OK
{

}

if () { // OK

} else {

}

if () { // Error

} else if () {

}

if () { // OK
} else if () {

} else {

}

/* Don't check
if () {
    if () {

    } else if () {

    } else () {
    }
} else if () {
    if () {

    }
    if () {

    } else if () {

    }
}

*/

while () {
    if () { // Error

    } else if () {

    }
}

if () { // Error
    if () { // OK

    } else if () {

    } else () {
    }
} else if () {
    if () { // OK

    }
    if () { // Error

    } else if () {

    }
}

