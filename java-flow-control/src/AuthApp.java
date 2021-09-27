
public class AuthApp {

	public static void main(String[] args) {
		System.out.println(args[0]);
		String id = "jm";
		String inputId = args[0];
		
		String pass = "1111";
		String inputPass = args[1];
		
		System.out.println("Hello");
		
		if(inputId.equals(id) && inputPass.equals(pass)) {
				System.out.println("Master!!");
			} else {
			System.out.println("Who r u??");
		}
	}

}
