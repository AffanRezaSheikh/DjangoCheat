# Week 1 — Responsive Registration Form

**Aim:** Build a responsive web application for a registration form which contains User Name, Password, Date of Birth, Gender, Mail-id, Contact Number, Address and a Submit button.

## Steps

1. **Make a folder** for the week, for example `week1`, and open it in VS Code (*File → Open Folder*).
2. **Write the static form.** Create [registration_static.html](open:week01-registration-form/registration_static.html). It uses plain HTML inputs: `text`, `password`, `date`, `radio`, `email`, `tel` (with `pattern="[0-9]{10}"`) and a `textarea`. Every field has `required`, so the browser blocks an empty submit.
3. **Open it in a browser** (double-click the file, or right-click → *Open with Live Server*). You get the unstyled form shown in [output/static-form.jpg](open:week01-registration-form/output/static-form.jpg).
4. **Write the responsive version.** Create [registration_responsive.html](open:week01-registration-form/registration_responsive.html). The `<style>` block:
   - centres the card with `display: flex; justify-content: center; align-items: center; min-height: 100vh`
   - limits the card to `max-width: 500px; width: 100%`
   - lays out the gender radios in a row with `.radio-inline { display: flex; gap: 20px }`
   - shrinks padding and heading size under 600px with `@media (max-width: 600px)`
5. **Add the submit script.** The `<script>` at the bottom stops the real submit with `event.preventDefault()` and shows *Form submitted successfully!*
6. **Test it.** Open the file, resize the window (or press `F12` → device toolbar) and check the layout at phone width. Compare with [output/responsive-form.jpg](open:week01-registration-form/output/responsive-form.jpg).
