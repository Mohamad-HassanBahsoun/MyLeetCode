class Solution {
    public int romanToInt(String s) {
        String roman = s;
        int number =0;
        for(int i = 0; i<roman.length(); i++){
            if(roman.charAt(i) == 'I'){
                if(i!= roman.length()-1) {
                    if ((roman.charAt(i + 1) == 'V' || roman.charAt(i + 1) == 'X')) {
                        number--;
                    } else {
                        number++;
                    }
                }else{
                    number++;
                }
            }else if(roman.charAt(i) == 'V'){
                number+= 5;
            }else if(roman.charAt(i) == 'X'){
                if(i!= roman.length()-1) {
                    if ((roman.charAt(i + 1) == 'L' || roman.charAt(i + 1) == 'C')) {
                        number -= 10;
                    } else {
                        number += 10;
                    }
                }else{
                    number+=10;
                }
            }else if(roman.charAt(i) == 'L'){
                number+= 50;
            }else if(roman.charAt(i) == 'C'){
                if(i!= roman.length()-1) {
                    if ((roman.charAt(i + 1) == 'M' || roman.charAt(i + 1) == 'D')) {
                        number -= 100;
                    } else {
                        number += 100;
                    }
                }else{
                    number+=100;
                }
            }else if(roman.charAt(i) == 'D'){
                number+= 500;
            }else if(roman.charAt(i) == 'M'){
                number+= 1000;
            }
        }
        return number;
        
    }
}