public class AccountingExample {	
	public static double Sales = 5000.0;
	public static double Cost = 4000.0;
	public static double getMR() {
		return 1 - (Cost / Sales);
	}
	public static double getMargin() {
		return Sales * getMR();
	}
	public static void main(String[] args) {
		System.out.println(Math.floor(getMargin()));
	}
}
