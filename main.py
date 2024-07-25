import module1_Speech_Detection
import module2_Speech_Recognition
import module3_Speech_Analysis
import module4_Answer
import module5_Text_To_Speech

def main():
    while True:
        print("Starting interaction cycle...")
        
        module1_Speech_Detection.module1()
        module2_Speech_Recognition.module2()
        module3_Speech_Analysis.module3()     
        module4_Answer.module4()
        module5_Text_To_Speech.module5()
        
        user_input = input("Do you want to continue the conversation? (y/n): ")
        if user_input.lower() != 'y':
            print("Exiting interaction cycle...")
            break

if __name__ == "__main__":   
    main()