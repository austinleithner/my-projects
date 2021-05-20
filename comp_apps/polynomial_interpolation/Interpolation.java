/**
  * this class calcuates values of a function using polynomial interpolation
  *
  * @author Austin Leithner
  * @version 11/8/2020
  *
  */
  

import java.util.*;
import java.lang.*;

public class Interpolation{
   private static final int N =20;//degree of polynomial
   private static double[] x = new double[N+1];
   private static double a =0.0;//start interval
   private static double b =2*Math.PI;//end interval
   private static double delx =(b-a)/N;
   
   private static double[] D = new double[N+1];
   
   private static final int n=100;
   private static double delz = (b-a)/n;
   private static double[] z = new double[n+1];
   
   public static void main(String[] args){
      double[] y = new double[n+1];
      
      //fills the x array
      for(int i=0; i<x.length;i++){
         x[i] = a +(i*delx);
      }
      //call coef to fill D array with the interpolating coeff
      coef();
      
      //fills the z array
      for(int i=0; i<z.length;i++){
         z[i] = a +(i*delz);
      }
      //loop through poly to find x,y values to graph using the z array and fills the y array
      for(int i=0; i<y.length;i++){
         y[i] = poly(z[i]);
      }
      
      
      //prints z array
      for(int i=0; i<z.length;i++){
         System.out.println(z[i]);
      }
      
      System.out.println();
      System.out.println();
      
      //used to test
      /*
      //prints y array
      for(int i=0; i<y.length;i++){
         System.out.println(y[i]);
      }
      
      System.out.println();
      System.out.println();
      //prints function value at z array
      for(int i=0; i<z.length;i++){
         System.out.println(f(z[i]));
      }
      */
      //calculates the error approx value used to graph and finds the max error
      double max=0;
      for(int i=0;i<y.length;i++){
         double temp = Math.abs(y[i]-f(z[i]));
         System.out.println(temp);
         if(temp>max){
            max=temp;
         }
      }
      
      System.out.println("max error: "+max);
      
   }
   
   //creates divided difference coeffs
   public static void coef(){
      for(int i=0;i<=N;i++){
         D[i] = f(x[i]);
      }
      
      for(int j=1;j<=N;j++){
         for(int i=N;i>=j;i--){
            D[i] = (D[i]-D[i-1])/(x[i]-x[i-j]);
         }
      }
      //return 0.0;
   }
   
   //calculates the approx function value at z
   public static double poly(double z){
      double[] p = new double[x.length];
      p[0]=1.0;
      for(int i=1;i<=N;i++){
         p[i]=(z-x[i-1])*p[i-1];
      }
      
      double sum=0;
      for(int i=0;i<=N;i++){
         sum+=D[i]*p[i];
      }
      
      return sum;
   }
   /*
   //e
   public static double f(double x){
      return Math.exp(x);
   }
   */
   /*
   //sine
   public static double f(double x){
      return Math.sin(x);
   }
   */
   /*
   //cosine
   public static double f(double x){
      return Math.cos(x);
   }
   */
   
   //sine^3
   public static double f(double x){
      return Math.pow(Math.sin(x),3);
   }
   
}