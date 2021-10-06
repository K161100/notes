#include<iostream>
using namespace std;
int main()
{
	int size, arr[1001], i, j, temp,s=0;
	cin>>size;
	for(i=0; i<size; i++)
	{
		cin>>arr[i];
	}
	for(i=1; i<size; i++)
	{
		temp=arr[i];
		j=i-1;
		while((temp<arr[j]) && (j>=0))
		{
			arr[j+1]=arr[j];
			s++;
			j=j-1;
		}
		arr[j+1]=temp;
	}
	cout<<s;
//	for(i=0; i<size; i++)
//	{
//		cout<<arr[i]<<" ";
//	}
}
