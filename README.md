# 🔐 Random Password Generator  

A simple Python-based **Password Generator** that creates secure, random passwords with customizable length and count.  
The program also gives you a **strength indicator** (weak, medium, strong) based on the chosen password length.  

-------

## ✨ Features  

- 🎲 **Random Password Generation** using Python's `random` module.  
- 🔡 Supports **letters (A–Z, a–z)**, **digits (0–9)**, and **special characters (!@#$%^& etc.)**.  
- 📏 Choose the **length** of your password.  
- 🔢 Generate **multiple passwords at once**.  
- 🛡️ **Password Strength Check**:  
  - Weak → Less than 6 characters.  
  - Medium → Between 6 and 9 characters.  
  - Strong → 10 or more characters.  
- ⚠️ Warns against generating more than 10 passwords at once (security tip).  

-------

## 📂 Project Structure  

 📁 PasswordGenerator
 
 ├── password_generator.py # Main script

--------

## 🔧 Requirements

- Python 3.x (no external libraries needed)

--------

## ▶️ Usage

                           Run the program in your terminal:  
                           python password_generator.py

--------

📊 Password Strength

                          Length	                   Strength
                          
                           < 6	                       Weak ❌

                           6 - 9	                    Medium ⚠️
                           
                           >= 10	                    Strong ✅

--------

🌟 Future Improvements

Add option to exclude/include special characters.

Add option to copy generated password(s) directly to clipboard.

Add a GUI interface for easier usage.
