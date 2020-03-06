/**
 * Epsilon
 */
public class Epsilon {

    public static void main(String[] args) {
        Epsilon eps = new Epsilon();
        eps.epsilon_double(0);
        eps.epsilon_float(0);
    }

    public void epsilon_double(int metodo){
        double d = 0.5;

        if (metodo == 1) {

            while ((1 + d) != 1)
            {
                System.out.println(d);
                d = d / 2;
            }
        }
        else
        {
            while (d!=0)
            {
                System.out.println(d);
                d = d / 2;
            }
        }
    }

    public void epsilon_float(int metodo) {
        float d = 0.5f;

        if (metodo == 1) {

            while ((1 + d) != 1)
            {
                System.out.println(d);
                d = d / 2;
            }
        }
        else
        {
            while (d!=0)
            {
                System.out.println(d);
                d = d / 2;
            }
        }
    }
}