// Desc:
// Author: Rebecca Miller
// Dates: Nov 11, 2025


var $ = function (id) {
  return document.getElementById(id);
};


// Define format options for printing.
const cur2Format = new Intl.NumberFormat("en-CA", {
  style: "currency",
  currency: "CAD",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});

const per2Format = new Intl.NumberFormat("en-CA", {
  style: "percent",
  minimumFractionDigits: "0",
  maximumFractionDigits: "2",
});

const com2Format = new Intl.NumberFormat("en-CA", {
  style: "decimal",
  minimumFractionDigits: "2",
  maximumFractionDigits: "2",
});


// Define program constants.
const FERT_TREAT_RATE = .03;
const BORDER_RATE = .28;
const LAWN_MOWING_RATE = .04;
const HST_RATE = .15;
const ENVIRO_RATE = .014;

// Start main program here.

let CustName = "John Smith" //prompt("Enter the customer name: ");
let StAdd = "123 Main St." //prompt("Enter the customer street address: ");
let City = "St. John's" //prompt("Enter the customer city: ");
let PhoneNum = "709-986-8240" //prompt("Enter the customer phone number (999-999-9999): ");
let TotSqaureFt = "1700" //prompt("Enter the total square feet for the property (99999): ");

let BorderCost = (TotSqaureFt * 0.04) * BORDER_RATE;
let MowingCost = (TotSqaureFt * 0.96) * LAWN_MOWING_RATE; 
let FertCost = FERT_TREAT_RATE * TotSqaureFt;

let TotCharges = BorderCost + MowingCost + FertCost;

let HSTCost = HST_RATE * TotCharges;
let SalesTax = TotCharges + HSTCost;

let EnviroTax = ENVIRO_RATE * TotCharges;
let InvoiceTot = TotCharges + EnviroTax + HSTCost;


// display the results using a table.
document.writeln("<br> </br>");
document.writeln("<table class='resultstable'>");

document.writeln("<tr>");
document.writeln("<td colspan= '2' class= 'orangeback'>Mo's Lawncare Services - Customer Invoice</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td colspan= '2' class= 'lefttext'><br />Customer Details<br />" + "<br />" + CustName + "<br />" + StAdd + "<br />" + City + "<br />" + PhoneNum + "<br />" + "<br />Property size" + " " + "(in sq ft):" + " " + TotSqaureFt + "<br />" + "<br />" + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class= 'lefttext' width= '200px'>Border cost:</td>");
document.writeln("<td class= 'righttext'>" + cur2Format.format(BorderCost) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class= 'lefttext'>Mowing cost:</td>");
document.writeln("<td class= 'righttext'>" + cur2Format.format(MowingCost) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class= 'lefttext'>Fertilizer cost:</td>");
document.writeln("<td class= 'righttext'>" + cur2Format.format(FertCost) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class= 'lefttext'>Total charges:</td>");
document.writeln("<td class= 'righttext'>" + cur2Format.format(TotCharges) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class= 'lefttext'>Sales tax (" + per2Format.format(HST_RATE) + "):</td>");
document.writeln("<td class= 'righttext'>" + cur2Format.format(HSTCost) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class= 'lefttext'>Environmental tax:</td>");
document.writeln("<td class= 'righttext'>" + cur2Format.format(EnviroTax) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td><br /></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class= 'lefttext'>Invoice total:</td>");
document.writeln("<td class= 'righttext'>" + cur2Format.format(InvoiceTot) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td colspan= '2' class= 'orangeback'>Turning Lawns into Landscapes</td>");
document.writeln("</tr>");

document.writeln("<table />")


































/*
document.writeln("<tr>");
document.writeln("<td width= '250px' class= 'lefttext'>Item name</td>");
document.writeln("<td class= 'righttext'>" + ItemName + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class= 'lefttext'>Item cost</td>");
document.writeln("<td class= 'righttext'>" + cur2Format.format(ItemCost) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class= 'lefttext'>Number in stock</td>");
document.writeln("<td class= 'righttext'>" + NumInStock + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td class= 'lefttext'></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class= 'lefttext'>Retail price</td>");
document.writeln("<td class= 'righttext'>" + cur2Format.format(RetPrice) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td class= 'lefttext'></td>");
document.writeln("</tr>");


document.writeln("<tr>");
document.writeln("<td class= 'lefttext'>Total inventory (Cost)</td>");
document.writeln("<td class= 'righttext'>" + cur2Format.format(TotInvCost) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class= 'lefttext'>Total inventory (Retail)</td>");
document.writeln("<td class= 'righttext'>" + cur2Format.format(TotInvRetail) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td class= 'lefttext'></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class= 'lefttext'>Gross margin</td>");
document.writeln("<td class= 'righttext'>" + cur2Format.format(GrossMargin) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td><br /></td>");
document.writeln("<td class= 'lefttext'></td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class= 'lefttext'>10% off price</td>");
document.writeln("<td class= 'righttext'>" + cur2Format.format(Sale10Off) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class= 'lefttext'>25% off price</td>");
document.writeln("<td class= 'righttext'>" + cur2Format.format(Sale25Off) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class= 'lefttext'>33% off price</td>");
document.writeln("<td class= 'righttext'>" + cur2Format.format(Sale33Off) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td class= 'lefttext'>50% off price</td>");
document.writeln("<td class= 'righttext'>" + cur2Format.format(Sale50Off) + "</td>");
document.writeln("</tr>");

document.writeln("<tr>");
document.writeln("<td colspan= '2' class= 'orangecenterrow'><br /></td>");
document.writeln("</tr>");

document.writeln("</table>");
*/