if () { // OK
    if () { // OK
        if () { // Error
            printf();
        }
        if () // Error
        {
            printf();
        }
        else
        {
            printf();
        }
    }
    if () { // OK
        if () { // Error
            printf();
        } else {

        }
        printf();
    } else {
        if () { // Error

        }
    }
    if () { // OK
        printf();
    } else if () { // OK
        if () { // Error

        }
    }
}

/* Don't check
if ()
{
    if ()
    {
        if () {
            printf();
        }
        if ()
        {
            printf();
        }
        printf();
    }
    if () {
        printf();
    }
}
*/

if () // OK
{
    if () // OK
    {
        if () { // Error
            printf();
        }
        if () // Error
        {
            printf();
        }
        printf();
    }
    if () { // OK
        printf();
    }
}

if () // OK
{
    if () // OK
    {
        // Code here
    }
    if () { // OK
        // Code here
    }
}
