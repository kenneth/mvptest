public class Machine extends Thread {

	public void run(){
		for(int a=0;a<50;a++)
			System.out.println(a);
	}

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Machine  machine = new Machine();
		machine.start();//machine
	}

}
