public class NumLetterCounts
{
   public static String[] unit = 
   { "","one","two","three","four","five","six","seven","eight","nine","ten",
      "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"
       
   };
 
   public static String[] tens = 
   {"","ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"
       
   };
 
   public static String[] hundreds = 
   {"","onehundred","twohundred","threehundred","fourhundred","fivehundred","sixhundred",
      "sevenhundred","eighthundred","ninehundred"
       
   }; 
     
   public int sumCounter(int number)
    {
         return inWords(number).length();
    }
 
    public String inWords(int number)
   {
      if(number < 20)
      {
         return unit[number];
      }
    
      else if(number < 100)
      {
            return tens[number/10] + inWords(number%10);
      }
    
      else 
      {
          String greaterThanHundred = "";
          greaterThanHundred = inWords(number % 100);
          if(greaterThanHundred.length() > 0)
          {
            greaterThanHundred = "and" + greaterThanHundred;
          }
              
          return hundreds[number/100] + greaterThanHundred;
      }
   }
      

      
     public static void main(String[] number)
     {
         NumLetterCounts countInst = new NumLetterCounts();
         int result = 11;
          
         for(int i = 1; i < 1000; i++)
         {
             result += countInst.sumCounter(i);
         }
          
         System.out.println("Sum of all the numbers from 1 to 1000 (one thousand) inclusive were written out in words: " + result);
     }
}