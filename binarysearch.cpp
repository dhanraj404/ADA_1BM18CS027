 #include<algorithm>
#include<iostream>
using namespace std;
int main()
{
	int n,i,j,k,ele,l,h,mid,a[50],count,fpos,lpos;
	cout<<"Enter the number of elements in array and element to be searched\n";
	cin>>n>>ele;
	l = 0;
	h = n-1;
	cout<<"Enter the elements of array\n";
	for(j=0;j<n;j++)
		cin>>a[j];
	sort(a, a+n);
	while(l<=h)
	{
		mid = (int)(l+h)/2;
		if(a[mid]==ele)
		{	
			i = mid;
			k = mid;			
			while(a[i]==ele)
			{			
				fpos = i;
				i--;
			}
			while(a[k]==ele)
			{
				lpos = k;
				k++;
			}
			cout<<"The first occurrence of the key is at "<<fpos<<" and last occurrence is at "<<lpos<<"\n";
			count = lpos-fpos+1;
			cout<<"The count is "<<count<<"\n";		
			break;
		}
		else if(a[mid]<ele)
			l = mid+1;
		else 
			h = mid-1;
	}
	if(l>h)
		cout<<"-1 (Element is not present)\n";
	return 0;
}
