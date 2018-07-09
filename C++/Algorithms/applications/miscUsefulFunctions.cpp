//helpful Functions

//****************************************************
// stringParser separates space-separated words from
// a sentence.
//****************************************************

int stringParser()
{
    string s = "scott tiger mushroom";
    string delimiter = " ";

    size_t pos = 0;
    string token;
    while ((pos = s.find(delimiter)) != string::npos)
    {
        cout << "Pos equals: " << pos << endl;
        token = s.substr(0, pos);
        cout << token << endl;
        s.erase(0, pos + delimiter.length());
    }
    cout << s << endl;
}