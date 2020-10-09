# project5CS50

This is an energy savings web application for households to efficiently use electricity. The application allows a client to input their number of household appliances. The application then calculates the household consumption estimation using heurestics. The client can save their appliance list (POST request) and they can compare their consumption to an average American household in the statistics section. The user can edit their appliance list (PUT request) and a new household consumption value will be calculated and the old list replaced if saved, the saved list can be viewed in the appliance list section (GET request), a client can not save more than one list. The client also has the option to delete their appliance list (DELETE request). I believe this project showcases all the skills I have learnt in this course:
- to create mobile responsive web application
- to create a single page web application, with HTML DOM control, createElement() and query selectors
- making asynchronous javascript requests (GET, POST, PUT, DELETE)
- an appliance list model was created
- utilised an external API, Energy Information Administration for informative data to the client
- calculator is user friendly, all technical energy values handled by the application
- implemented Bootstrap JS modals to improve user experience and functionality