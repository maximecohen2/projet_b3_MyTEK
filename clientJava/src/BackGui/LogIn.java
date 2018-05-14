package BackGui;

public class LogIn extends DataBackEnd {
	private org.json.JSONObject myLog = new org.json.JSONObject();
	private org.json.JSONObject returnApi = new org.json.JSONObject();

	
	public LogIn(String Name, String mdp){
		myLog.put("Name", Name).toString();
		myLog.put("Mdp", mdp).toString();
		sendLogIn();
	}

	private void sendLogIn() {
		// TODO
		// returnApi = connexion to the API
		DataBackEnd.setMyToken("retourApi");
	}
	
	public String getMyLog() {
		return myLog.toString();
	}
	
	@Override
	public String toString() {
		return myLog.toString();
	}
	
	public static void main(String[] args) {
		LogIn toto = new LogIn("Cedric", "Clemenceau");
		
		System.out.println(toto);
	}
}
