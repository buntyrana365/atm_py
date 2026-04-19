function validateAmount(fieldId) {
  const input = document.getElementById(fieldId);
  if (!input) {
    return true;
  }

  const value = parseFloat(input.value);
  if (Number.isNaN(value) || value <= 0) {
    alert("Please enter a valid amount greater than zero.");
    input.focus();
    return false;
  }

  return true;
}
