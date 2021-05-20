/**
 / This program prints 100 points for sine x cosine x and tangent x within a given range
 /
 /
 / @author Austin Leithner
 / @version 9/14/20
 */
import java.util.*;
import java.lang.*;

public class Trig{

   public static final double eps = Math.pow(10.0,-15.0); //absolute error

   public static void main(String[] args){
      double[] x= new double[101];
      double[] y= new double[101];
      /*
      //fill the x array with the range 0-2pi with 100 points
      for(int i =0;i<x.length;i++){
         x[i]=((2*Math.PI)/100.0)*(i);
      }
      */
      
      double psi = 0.1;
      //fills the x array with the range -pi/2 - pi/2
      for(int i =0;i<x.length;i++){
         x[i]=(-(Math.PI)/2)+psi+(((Math.PI-(2*psi))/100.0)*(i));
      }
      
      /*
      //fills the y array with sine x values
      for(int i =0;i<y.length;i++){
         y[i]=sine(x[i]);
      }
      */
      /*
      //fills the y array with cosine x values
      for(int i =0;i<y.length;i++){
         y[i]=cosine(x[i]);
      }
      */
      
      
      //fills the y array with tangent x values
      for(int i =0;i<y.length;i++){
         y[i]=sine(x[i])/cosine(x[i]);
      }
      
      //prints the x and y array to be copied into excel
      for(int i =0;i<y.length;i++){
         System.out.println(x[i]);
         
      }
      System.out.println();
      for(int i =0;i<y.length;i++){
         
         System.out.println(y[i]);
      }
   }
   
   //calculates sine x
   public static double sine(double x){
      double sum1=x;
      double sum2=x-((1.0/6.0)*Math.pow(x,3.0)) ;
      int n=2;
      while(Math.abs(sum2-sum1)>eps){
         sum1=sum2;
         sum2+=(Math.pow(-1.0,n)/(1.0*nfact((2*n)+1)))*(Math.pow(x,(2*n)+1));
         n++;
      }
      return sum1;
   }
   
   //calculates cosine x
   public static double cosine(double x){
      double sum1=1;
      double sum2=1-((1.0/2.0)*Math.pow(x,2.0)) ;
      int n=2;
      while(Math.abs(sum2-sum1)>eps){
         sum1=sum2;
         sum2+=(Math.pow(-1.0,n)/(nfact(2*n)))*(Math.pow(x,(2*n)));
         n++;
      }
      return sum1;
   }
   
   //calculates n-factoral using recursion
   public static double nfact(double n){
      if(n==0){return 1;}
      return n*nfact(n-1);
   }
}