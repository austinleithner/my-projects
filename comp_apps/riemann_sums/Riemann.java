/**
  * this class aproximates a definite integral using riemann summs
  *
  * @author Austin Leithner
  * @version 11/23/2020
  *
  */
  

import java.util.*;
import java.lang.*;

public class Riemann{
   private static final double eps=Math.pow(10,-6);//error
   private static double a =0.0;//start interval
   private static double b =Math.PI;//end interval
   private static double exact = (Math.exp(Math.PI)+1)/2;//the exact value of the definate integral
   private static int n = 1000;//number of iterations
   
   public static void main(String[] args){
      
      System.out.println(Math.abs(rect(n)-exact));
      
      System.out.println(Math.abs(mid(n)-exact));
      
      System.out.println(Math.abs(trap(n)-exact));
      
      System.out.println(Math.abs(rectcau()-exact));
      
      System.out.println(Math.abs(midcau()-exact));
   }
   
   
   //rectangle
   public static double rect(int n){
      double delx =(b-a)/n;
      double I=0;
      for(int i=0;i<=n-1;i++){
         I+=f(a+i*delx);
      }
      return I*delx;
   }
   
   //madpoint
   public static double mid(int n){
      double delx =(b-a)/n;
      double I=0;
      for(int i=0;i<=n-1;i++){
         I+=f(a+((i+(1/2))*delx));
      }
      return I*delx;
   }
   
   //trapezoid
   public static double trap(int n){
      double delx =(b-a)/n;
      double I=(1/2)*(f(a)+f(a));
      for(int i=1;i<=n-1;i++){
         I+=f(a+i*delx);
      }
      return I*delx;
   }
   
   //rectangle using Cauchy criterion
   public static double rectcau(){
      
      double I1 = (b-a)*f(a);
      double I2 = (b-a)*(f(a)+f((a+b/2)));
      int N = 3;
      while(Math.abs(I1-I2)>eps){
         I1=I2;
         double delx =(b-a)/N;
         I2=0;
         for(int i=0;i<=N-1;i++){
            I2+=f(a+(i*delx));
         }
         I2*=delx;
         N++;
      }
      return I1;
   }
   
   //midpoint using Cauchy criterion
   public static double midcau(){
      
      double I1 = (b-a)*f((a+b)/2);
      double I2 = (b-a)*(f((a+b)/4)+f((a+(3*b)/4)));
      int N = 3;
      while(Math.abs(I1-I2)>eps){
         I1=I2;
         double delx =(b-a)/N;
         I2=0;
         for(int i=0;i<=N-1;i++){
            I2+=f(a+((i+(1/2))*delx));
         }
         I2*=delx;
         N++;
      }
      return I1;
   }
   
   //e^x * sine x
   public static double f(double x){
      return Math.exp(x) * Math.sin(x);
   }
   
   /*
   //sine
   public static double f(double x){
      return Math.sin(x);
   }
   */
   /*
   //sine^3
   public static double f(double x){
      return Math.pow(Math.sin(x),3);
   }
   */
}