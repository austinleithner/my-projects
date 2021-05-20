/**
 / this class calculates the roots of the provided functions using the bisection method
 /
 / @author Austin Leithner
 / @version 10/8/20
**/
import java.lang.*;

public class roots{
   private static final double eps = Math.pow(10,-15);
   
   public static void main(String [] args){
      System.out.println(bisect(3,4));//3.141592653589793 n=47
      //sine at 3,4
      
      //System.out.println(bisect(1,2));//1.414213562373095 n=49
      //root two at 1,2
      
      //System.out.println(bisect(-2,0));//-1.2469796037174672 n=51
      //System.out.println(bisect(0,1));//0.4450418679126287 n=46
      //System.out.println(bisect(1,2));//1.801937735804838 n=47
      //intersect at -2,0 0,1 1,2
      
      //System.out.println(bisect(-1,1));//0 n=0
      //System.out.println(bisect(2,3));//the graph shows a root at 2,3 when I ran the code I wwas getting a long search time with no results the graph root is ~2.319
      //exp at -1,1 2,3
   }
   
   public static double bisect(double a, double b){
      double xi = (a+b)/2;
      int n =0;
      while(Math.abs(sine(xi))>eps){//function at xi
         if((sine(xi)*sine(a))<0){b=xi;}
         else{a=xi;}
         xi=(a+b)/2;
         n++;
      }
      System.out.println(n);
      return xi;
   }
   
   public static double sine(double x){return Math.sin(x);}
   
   /*
   public static double bisect(double a, double b){
      double xi = (a+b)/2;
      int n =0;
      while(Math.abs(rootTwo(xi))>eps){//function at xi
         if((rootTwo(xi)*rootTwo(a))<0){b=xi;}
         else{a=xi;}
         xi=(a+b)/2;
         n++;
      }
      System.out.println(n);
      return xi;
   }
   public static double rootTwo(double x){return Math.pow(x,2)-2;}
   */
   /*
   public static double bisect(double a, double b){
      double xi = (a+b)/2;
      int n =0;
      while(Math.abs(intersect(xi))>eps){//function at xi
         if((intersect(xi)*intersect(a))<0){b=xi;}
         else{a=xi;}
         xi=(a+b)/2;
         n++;
      }
      System.out.println(n);
      return xi;
   }
   public static double intersect(double x){return Math.pow(x,3)-Math.pow(x,2)-(2*x)+1;}
   */
   /*
   public static double bisect(double a, double b){
      double xi = (a+b)/2;
      int n =0;
      while(Math.abs(exp(xi))>eps){//function at xi
         if((exp(xi)*exp(a))<0){b=xi;}
         else{a=xi;}
         xi=(a+b)/2;
         n++;
      }
      System.out.println(n);
      return xi;
   }
   public static double exp(double x){return 6+Math.pow(3*x,2)+Math.pow(2*x,3)-(6*(Math.exp(x)-x));}
   */
}