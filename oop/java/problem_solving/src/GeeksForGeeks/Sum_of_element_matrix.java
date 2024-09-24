package GeeksForGeeks;

public class Sum_of_element_matrix {
	static int sum(int N,int M,int [][]Grid) {
		int sum=0;
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				sum=sum+Grid[i][j];
			}
		}
		
		return sum;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int N=2,M=3,Grid[][]= {{1,0,1},{-8,9,-2}};
		int x=3,y=5,grid[][]= {{1,0,1,0,1},{0,1,0,1,0},{-1,-1,-1,-1,-1}};
		System.out.println(sum(N,M,Grid));
		System.out.println(sum(x,y,grid));

	}

}

//Input:
//N=2,M=3
//Grid=
//[[1,0,1],
//[-8,9,-2]]
//Output:
//1
//Explanation:
//The sum of all elements of the matrix is 
//(1+0+1-8+9-2)=1.

//Input:
//N=3,M=5
//Grid=
//[[1,0,1,0,1],
//[0,1,0,1,0],
//[-1,-1,-1,-1,-1]]
//Output:
//0
//Explanation:
//The sum of all elements of the matrix are
//(1+0+1+0+1+0+1+0+1+0-1-1-1-1-1)=0.