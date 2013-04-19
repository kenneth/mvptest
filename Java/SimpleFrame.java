import java.awt.*;
public class SimpleFrame {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
	Frame f = new Frame("hello");
	f.add(new Button("Press Me"));
	f.setSize(100,100);//设置Frame的宽和高
	f.setVisible(true);//使Frame变为可见
	}

}
