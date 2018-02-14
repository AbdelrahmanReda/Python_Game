#include <iostream>
#include<bits/stdc++.h>
using namespace std;
int p1=0;
int p2=0;
int detecting_player = 0;
int x1,x2;
int main()
{ srand(time(0));

     //---the ----


//-------
char letter_list[20] = {'A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F', 'G', 'G', 'H', 'H', 'I', 'I', 'J', 'J'};



for (int c =0; c< 20; c++)
  {
        int r = rand()%20;
        char temp=letter_list[c];
        letter_list[c]=letter_list[r];
        letter_list[r]=temp;


  }









char numbers[20] ={'1','2','3','4','5','6','7','8','9','0','1','2','3','4','5','6','7','8','9','0'};
string numbers_list="12345679801324567890";
while (true)
{
    if (detecting_player %2==0)
    {
      cout<<"player one turn"<<endl;
    }
    else
    {
      cout<<"player one turn"<<endl;
    }

while (true)
{
   if (detecting_player % 2 == 0)

 {  cout<<"please enter the first number"<<endl;
    cin>>x1;
    cout<<"please enter the second number"<<endl;
    cin>>x2;
 }
   else
   {
    cout<<"please enter the first number"<<endl;
    cin>>x1;
    cout<<"please enter the second number"<<endl;
    cin>>x2;
   }
   if( x1 <21 && x2 <21 && x1!=x2 && x1 != 0 && x2 != 0)
   {
      if( numbers[x1-1] =='*' || numbers[x2-1]=='*')

      {
          _sleep(0.5);
       cout<<"please enter valid numbers"<<endl;
       cout<<"please enter the first number"<<endl;
       cin>>x1;
       cout<<"please enter the second number"<<endl;
       cin>>x2;      }

   }
   else
   {
     _sleep(1500);
     cout<<"please enter valid numbers"<<endl;
     cout<<"please enter the first number"<<endl;
     cin>>x1;
     cout<<"please enter the second number"<<endl;
     cin>>x2;
   }
   //print(x1,x2)
    numbers_list[x1 - 1] = letter_list[x1 - 1];
    numbers_list[x2 - 1] = letter_list[x2 - 1];
    for (int q=0;q<numbers_list.length();q++)
    {
        cout<<numbers_list[q]<<" ";
    }
    _sleep(1500);
    cout<<"\r";

  //checking for equality
    if( letter_list[x1 - 1]==letter_list[x2-1])
      {
       numbers[x1 - 1] = '*';
       numbers[x2 - 1] = '*';
    if (detecting_player % 2 == 0)
        {p1=p1+1;
        }
    else
        {p2=p2+1;
        }
    for (int y=0;y<20;y++)
    {
        cout<<numbers[y]<<" ";
    }
    cout<<endl;

}
else
    {
    for (int z=0;z<20;z++)
    {
        cout<<numbers[z]<<" ";
    }
    cout<<endl;


    }
    cout<<"player 1:"<<p1<<" " <<"player 2:"<< p2<<endl;
     detecting_player++;
         if (p1 > 5)
       {cout<<"p1ayer 1  is the winnner"<<endl;
        break;}
    else if (p2 > 5)
        {cout<<"player 2  is the winnner"<<endl;
        break;}
    else if (p1 + p2 == 10)
        {cout<<"draw"<<endl;
        break;}
    cout<<"=========================="<<endl;
}
    return 0;
}
}
