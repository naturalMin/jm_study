
public class timestable {

	public static void main(String[] args) {
		int arr[][] = new int[9][9];
		for(int i = 0; i < 9; i++) {
			for(int j = 0; j < 9; j++) {
				arr[i][j] = (i+1) * (j+1);
				System.out.print(arr[i][j]+" ");
			}
			System.out.println();
		}
		

	}

}
