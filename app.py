@app.route("/workshop", methods=["GET", "POST"])
def workshop():
    """Handle encryption and decryption requests."""
    result = ""
    original = ""
    error = ""

    if request.method == "POST":
        try:
            # Get form data
            original = request.form.get("message", "")
            action = request.form.get("action", "encrypt")

            # Validate message is not empty
            if not original.strip():
                error = "Please enter a message to encrypt or decrypt."
            else:
                # Build the key from form inputs
                key = {
                    "shift": int(request.form.get("shift", 5)),
                    "block_size": int(request.form.get("block_size", 4)),
                    "password": request.form.get("password", "SECRET"),
                    "noise_interval": int(request.form.get("noise_interval", 3)),
                    "noise_char": request.form.get("noise_char", "~"),
                }

                # Perform the operation
                if action == "encrypt":
                    result = encrypt(original, key)
                else:
                    result = decrypt(original, key)
        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template(
        "workshop.html", result=result, original=original, error=error
    )
