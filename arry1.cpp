#include <iostream.h>
const int MAX =5;

class array
{
    private:
int arr[MAx];
public:
void insert(int pos , int num)
void del(int pos);
void reverse();
void display();
void search(int num);
};

void array:: insert(int pos , int num)
{
    for (int i=MAX-1; i>=pos ; i--)
    {
        arr[i-1]=arr[i];
        arr[i-1]=0;
    }
}

void array::  reverse()
{
    for (int i=0; i<MAX/2; i++)
    {
        int temp = arr[i];
        arr[i]=arr[MAX-1-i];
        arr[MAX-1-i]=temp;
    }
}
    
void array::search(int num)
{
    for (int i=0; i<MAX; i++)
    {
        if (arr[i]==num)
        {
            cout<<"Element found at position: "<<i<<endl;
            return;
        }
    }
    cout<<"Element not found"<<endl;
}
void array:: display()
{
    for (int i=0; i<MAX; i++)
    {
        cout<<arr[i]<<" ";
    }
    cout<<endl;
}
void array:: del(int pos)
{
    for (int i=pos; i<MAX-1; i++)
    {
        arr[i]=arr[i+1];
    }
    arr[MAX-1]=0;
}
int main()
{
    array a;
    a.insert(2,10);
    a.display();
    a.delete(3);
    a.display();
    a.reverse();
    a.display();
    a.search(10);
    return 0;
}