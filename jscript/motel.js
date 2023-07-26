// Create a MotelCustomer object
const MotelCustomer = {
  name: "John Doe",
  birthDate: "1990-05-15",
  gender: "Male",
  roomPreferences: ["Single", "Non-smoking", "King-sized bed"],
  paymentMethod: "Credit Card",
  mailingAddress: {
    street: "123 Main St",
    city: "New York",
    state: "NY",
    postalCode: "10001",
  },
  phoneNumber: "555-123-4567",
  checkIn: {
    date: "2023-07-24",
    time: "15:00",
  },
  checkOut: {
    date: "2023-07-28",
    time: "11:00",
  },
  // Method to calculate the age of the customer
  calculateAge: function () {
    const birthYear = new Date(this.birthDate).getFullYear();
    const currentYear = new Date().getFullYear();
    return currentYear - birthYear;
  },
  // Method to calculate the duration of stay
  calculateDurationOfStay: function () {
    const checkInDate = new Date(this.checkIn.date);
    const checkOutDate = new Date(this.checkOut.date);
    const durationInMilliseconds = checkOutDate - checkInDate;
    const durationInDays = durationInMilliseconds / (1000 * 60 * 60 * 24);
    return durationInDays;
  },
  // Method to generate a description of the customer
  generateDescription: function () {
    return `
      Name: ${this.name}\n
      Age: ${this.calculateAge()}\n
      Gender: ${this.gender}\n
      Room Preferences: ${this.roomPreferences.join(", ")}\n
      Payment Method: ${this.paymentMethod}\n
      Mailing Address: ${this.mailingAddress.street}, ${this.mailingAddress.city}, ${this.mailingAddress.state}, ${this.mailingAddress.postalCode}\n
      Phone Number: ${this.phoneNumber}\n
      Check-in Date: ${this.checkIn.date} at ${this.checkIn.time}\n
      Check-out Date: ${this.checkOut.date} at ${this.checkOut.time}\n
      Duration of Stay: ${this.calculateDurationOfStay()} days
    `;
  },
};

// Call the generateDescription method to get the customer description
// const customerDescription = MotelCustomer.generateDescription();

// // Print the customer description
// console.log(customerDescription);


// Your MotelCustomer object and other JavaScript code (as shown in the previous example)

// Get the element where you want to display the customer information
const customerInfoElement = document.getElementById("customerInfo");

// Call the generateDescription method to get the customer description
const customerDescription = MotelCustomer.generateDescription();

// // Update the content of the HTML element with the customer information
// customerInfoElement.textContent = customerDescription;

// Split the customerDescription by newline character and join with <br> to add line breaks
const formattedDescription = customerDescription.split('\n').join('<br>');

// Update the content of the HTML element with the customer information
customerInfoElement.innerHTML = formattedDescription;

console.log(customerDescription);