
import java.awt.*;
import java.awt.event.*;
//import java.awt.Action
class Awt{
    Frame f1;
    Awt(){
        f1=new Frame("Rithk");
        f1.setSize(700,700);
        f1.setVisible(true);
        f1.setBackground(Color.WHITE); 
        f1.setLayout(null);
        Label l1=new Label("Allotment");
        l1.setBounds(150, 50, 200, 40);
        l1.setFont(new Font("Arial",Font.BOLD,24));
        Button b1=new Button("Next");
        b1.setBounds(200, 100, 100, 100);
        f1.add(l1);
        f1.add(b1);
        f1.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e){
                System.exit(0);
            }
        });
        

    }


   public static void main(String[] args){
    new Awt();
}
}