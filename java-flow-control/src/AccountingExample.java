//class
class AccountingMargin {
	public double Sales;
	public double Cost;
	//init
	public AccountingMargin(double Sales, double Cost) {
		this.Sales = Sales;
		this.Cost = Cost;
	}
	public double getMR() {
		return 1 - (Cost / Sales);
	}
	public double getMargin() {
		return Sales * getMR();
	}
}
public class AccountingExample {	
	
	public static void main(String[] args) {
		//instance
		AccountingMargin m1 = new AccountingMargin(10000.0, 5000.0);
		AccountingMargin m2 = new AccountingMargin(20000.0, 6000.0);
		System.out.println(Math.floor(m1.getMargin()));
		System.out.println(Math.floor(m2.getMargin()));
	}
}
