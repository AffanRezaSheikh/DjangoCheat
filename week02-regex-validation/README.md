# Week 2 — Validate the Registration Page with Regular Expressions

**Aim:** Write a JavaScript program to validate the registration page using regular expressions.

## Steps

1. **Create the form.** Make [registration_validation.html](open:week02-regex-validation/registration_validation.html). The fields have **no** `required` attributes, so all checking is done by JavaScript.
2. **Collect the values** inside the `submit` listener with `document.getElementById(...).value.trim()`. Gender is read with `document.querySelector('input[name="gender"]:checked')`.
3. **Define the patterns:**

   | Field | Regular expression | Rule |
   |---|---|---|
   | User Name | `/^[A-Za-z0-9_]{3,15}$/` | 3–15 letters, numbers or underscores |
   | Password | `/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{6,}$/` | at least 6 characters, at least 1 letter and 1 number |
   | Mail-id | `/^[^\s@]+@[^\s@]+\.[^\s@]+$/` | basic `name@domain.ext` format |
   | Contact Number | `/^[0-9]{10}$/` | exactly 10 digits |

4. **Check each field in order** with `regex.test(value)`. On the first failure show an `alert(...)` and `return`. Date of Birth and Gender only need to be filled; Address must be at least 5 characters.
5. **Show success** with *Form submitted successfully!* when every check passes.
6. **Test it** with a bad user name such as `ab` — you should see the alert in [output/invalid-username-alert.jpg](open:week02-regex-validation/output/invalid-username-alert.jpg).
