/**
 / this class calculates the roots of the provided functions using Newton's method
 /
 / @author Austin Leithner
 / @version 10/21/20
**/
import java.lang.*;

public class NewtonRoot{
   private static final double eps = Math.pow(10,-15);
   
   public static void main(String [] args){
      //System.out.println(newton(3,4));//3.141592653589793 n=3
      //sine at 3,4
      
      //System.out.println(newton(1,2));//1.4142135623730951 n=4
      //root two at 1,2
      
      //System.out.println(newton(-2,0));//-1.246979603717467 n=5
      //System.out.println(newton(0,1));//0.4450418679126284 n=3
      //System.out.println(newton(1,2));//1.8019377358048383 n=6
      //intersect at -2,0 0,1 1,2
      
      //System.out.println(newton(-1,1));//0.0 n=0
      //System.out.println(newton(2,3));//2.318581709660071 n=61
      //exp at -1,1 2,3
      
      System.out.println(newton(4,5));//4.493409457909064 n=4
      //tan at 4,5
   }
   
   public static double newton(double a, double b){
      double xi = (a+b)/2;
      int n =0;
      while(Math.abs(f(xi))>eps){//function at xi
         xi=xi-(f(xi)/fp(xi));
         n++;
      }
      System.out.println(n);
      return xi;
   }
   //sine
   //public static double f(double x){return Math.sin(x);}
   //public static double fp(double x){return Math.cos(x);}
   
   
   //rootTwo
   //public static double f(double x){return Math.pow(x,2)-2;}
   //public static double fp(double x){return 2*x;}
   
   
   //intersect
   //public static double f(double x){return Math.pow(x,3)-Math.pow(x,2)-(2*x)+1;}
   //public static double fp(double x){return (3*Math.pow(x,2))-(2*x)-2;}
   
   
   //exp
   //public static double f(double x){return 6+(3*Math.pow(x,2))+(2*Math.pow(x,3))-(6*(Math.exp(x)-x));}
   //public static double fp(double x){return 6*(x+Math.pow(x,2)-Math.exp(x)-1);}
   
   //tan
   public static double f(double x){return Math.tan(x)-x;}
   public static double fp(double x){return Math.pow((1/Math.cos(x)),2)-1;}
}