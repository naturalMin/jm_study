
public class LoopStar {

	public static void main(String[] args) {
		//마름모로 별 찍기
		for(int i = 0; i < 5; i++) {
			for(int j = 0; j < 4-i; j++) {
				System.out.print(" ");
			}
			for(int j = 0; j < 2*i+1; j++ ) {
				System.out.print("*");
			}
			System.out.println("");
		}
		for(int k = 4; k > 0; k--) {
			for(int m = 0; m < 5-k; m++) {
				System.out.print(" ");
			}
			for(int m = 0; m < 2*k-1; m++) {
				System.out.print("*");
			}
			System.out.println("");
		}
	}
}
