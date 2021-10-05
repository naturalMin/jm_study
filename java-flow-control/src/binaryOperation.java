import java.util.Scanner;

public class binaryOperation {

	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		int a[] = new int[8];
		int i = 0;
		int n = scan.nextInt();
		while( n > 0 ) {
			a[i++] = n % 2;
			n /= 2;
		}
		scan.close();
		for(i = 7; i >= 0; i--) {
			System.out.print(a[i]);			
		}		
	}
}
