# **Database Design**

## **User Dashboard**
```
This is list of user will have dashboard to use the system:
1. Customer (Service Users)
2. Spa Owner (Vendor)
3. Staff (Vendor’s Employees):
4. Marketing Content Manager
3. System Administrator
```


## **User Database Component**
```
List of table will have for User:
1. Customer
2. Customer Preferences
3. Customer Appointments
4. Customer Payment History
```


```
Customer Table:

| Field Name              | Description                                               | Filled By                |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Customer ID             | A unique identifier for each customer.                    | System                   |
| First Name              | The customer’s first name.                                | Customer                 |
| Last Name               | The customer’s last name.                                 | Customer                 |
| Email                   | The customer’s email address for login and communication. | Customer                 |
| Password                | The password chosen by the customer.                      | Customer                 |
| Phone Number            | The customer’s contact number.                            | Customer                 |
| Address                 | Customer's physical address. (Optional)                   | Customer                 |
| Date of Birth           | For promotions or personalized services. (Optional)       | Customer                 |
| Profile Image           | Customer's profile picture. (Optional)                    | Customer                 |
| Created Date            | Date when the account was created.                        | System                   |
| Last Updated            | The last update to the profile. (Generated Automatically) | System                   |
| Account Status          | Indicates whether the account is active or inactive.      | System                   |
```

```
Customer Preferences:

|      Field Name            | Description                                                 | Filled By           |
|----------------------------|-------------------------------------------------------------|--------------------------|
| Preference ID              | A unique identifier for each preference record.             | System                   |
| Customer ID                | Links to the customer’s profile.                            | System                   |
| Communication Preference   | How the customer prefers to receive notifications (email, SMS) | Customer                 |
| Saved Payment Methods      | List of saved payment options for future use. (Optional)     | Customer                 |
| Favorite Services          | Services the customer has marked as favorites. (Optional)    | Customer                 |
| Notification Preferences   | Controls what types of notifications the customer receives (promotions, reminders). (Optional) | Customer|
```


```
Customer Appointments:
| **Field Name**         | **Description**                                           | **Filled By**            |
|------------------------|-----------------------------------------------------------|--------------------------|
| Appointment ID         | A unique identifier for each appointment. (Generated Automatically) | System                   |
| Customer ID            | Links to the customer’s profile.                           | System                   |
| Service ID             | The specific service booked by the customer.               | Customer/System          |
| Vendor ID              | The spa or salon where the service is booked.              | System                   |
| Appointment Date       | The date and time chosen for the appointment.              | Customer                 |
| Status                 | Current status of the appointment (confirmed, canceled, rescheduled, completed). | Customer/System          |
| Review                 | Feedback provided by the customer after the service. (Optional) | Customer                 |
```


```
Customer Payment History:
| **Field Name**         | **Description**                                           | **Filled By**            |
|------------------------|-----------------------------------------------------------|--------------------------|
| Payment ID             | A unique identifier for each payment. (Generated Automatically) | System                   |
| Customer ID            | Links to the customer’s profile.                           | System                   |
| Appointment ID         | Links to the related service appointment.                  | System                   |
| Payment Method         | The method of payment used (credit card, PayPal).          | Customer                 |
| Total Amount           | The total amount paid for the service, including taxes or discounts. (Generated Automatically) | System                   |
| Payment Date           | The date the payment was processed. (Generated Automatically) | System                   |
| Receipt                | A record of the payment details, available for download.   | System                   |
```


## **Vendor Database Component**
```
List of table will have for Vendor:
1. Vendor
2. Vendor Services
3. Vendor Staff
4. Vendor Appointments
```

```
Vendor Table:

| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Vendor ID               | A unique identifier for each vendor (spa/salon owner). (Generated Automatically) | System                   |
| Business Name           | The name of the spa or salon.                             | Vendor                   |
| Owner First Name        | First name of the business owner.                         | Vendor                   |
| Owner Last Name         | Last name of the business owner.                          | Vendor                   |
| Email                   | Email address for login and communication.                | Vendor                   |
| Password                | Password chosen for login. (Stored securely)              | Vendor                   |
| Phone Number            | Contact phone number for the business.                    | Vendor                   |
| Business Address        | Location of the business.                                 | Vendor                   |
| Logo                    | The logo of the business. (Optional)                     | Vendor                   |
| Created Date            | Date when the account was created. (Generated Automatically) | System                   |
| Last Updated            | The last time the profile was updated. (Generated Automatically) | System                   |
| Account Status          | Indicates whether the vendor’s account is active or inactive. | System                   |

```


```
Vendor Services Table:

| **Field Name**         | **Description**                                           | **Filled By**            |
|------------------------|-----------------------------------------------------------|--------------------------|
| Service ID             | A unique identifier for each service. (Generated Automatically) | System                   |
| Vendor ID              | Links to the vendor’s profile.                            | System                   |
| Service Name           | The name of the service (e.g., massage, facial).           | Vendor                   |
| Description            | Detailed description of the service.                      | Vendor                   |
| Price                  | The cost of the service.                                  | Vendor                   |
| Duration               | Length of time required for the service (in minutes).      | Vendor                   |
| Category               | Type of service (e.g., haircare, skincare).               | Vendor                   |
| Availability           | Whether the service is available for booking.             | Vendor                   |
```

```
Vendor Staff Table:

| **Field Name**         | **Description**                                           | **Filled By**            |
|------------------------|-----------------------------------------------------------|--------------------------|
| Staff ID               | A unique identifier for each staff member. (Generated Automatically) | System                   |
| Vendor ID              | Links to the vendor’s profile.                            | System                   |
| Staff First Name       | First name of the staff member.                           | Vendor                   |
| Staff Last Name        | Last name of the staff member.                            | Vendor                   |
| Role                   | Job role or position (e.g., masseuse, hair stylist).      | Vendor                   |
| Schedule               | Working hours and availability of the staff member.       | Vendor                   |
| Is Active              | Indicates if the staff member is currently employed and active. | Vendor                   |
| Created Date           | Date when the staff profile was created. (Generated Automatically) | System                   |
```


```
Vendor Appointments Table:
| **Field Name**         | **Description**                                           | **Filled By**            |
|------------------------|-----------------------------------------------------------|--------------------------|
| Appointment ID         | A unique identifier for each appointment. (Generated Automatically) | System                   |
| Vendor ID              | Links to the vendor’s profile.                            | System                   |
| Staff ID               | The staff member assigned to the appointment.             | System                   |
| Customer ID            | The customer who booked the appointment.                  | System                   |
| Service ID             | The service that is being provided.                       | System                   |
| Appointment Date       | Date and time of the appointment.                         | Customer                 |
| Status                 | Status of the appointment (confirmed, canceled, rescheduled, completed). | Vendor/Customer/System   |
```


```
Vendor Promotions Table:
| **Field Name**         | **Description**                                           | **Filled By**            |
|------------------------|-----------------------------------------------------------|--------------------------|
| Promotion ID           | A unique identifier for each promotion. (Generated Automatically) | System                   |
| Vendor ID              | Links to the vendor’s profile.                            | System                   |
| Promotion Code         | Code used for customers to avail discounts.               | Vendor                   |
| Discount Percentage    | Percentage of the discount offered.                       | Vendor                   |
| Start Date             | Date when the promotion starts.                           | Vendor                   |
| End Date               | Date when the promotion ends.                             | Vendor                   |

```


```
Vendor Payment Summary Table:

| **Field Name**         | **Description**                                           | **Filled By**            |
|------------------------|-----------------------------------------------------------|--------------------------|
| Payment ID             | A unique identifier for each payment. (Generated Automatically) | System                   |
| Vendor ID              | Links to the vendor’s profile.                            | System                   |
| Customer ID            | Links to the customer who made the payment.               | System                   |
| Appointment ID         | Links to the associated appointment.                      | System                   |
| Total Amount Received  | Total payment received from the customer. (Generated Automatically) | System                   |
| Payment Method         | Method used for the payment (credit card, PayPal).        | Customer                 |
| Payment Date           | Date the payment was made. (Generated Automatically)      | System                   |
```

## **Staff Database Component**
```
List of table will have for Vendor:
1. Staff Table
2. Staff Schedule Table
3. Staff Appointments Table
4. Staff Performance Metrics Table
5. Staff Payroll Table
```

```
Staff Table:

| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Staff ID                | A unique identifier for each staff member. (Generated Automatically) | System                   |
| Vendor ID               | Links the staff member to the spa/salon they work for.     | System                   |
| Staff First Name        | First name of the staff member.                           | Vendor                   |
| Staff Last Name         | Last name of the staff member.                            | Vendor                   |
| Role                    | The job role or position (e.g., hair stylist, masseuse).  | Vendor                   |
| Email                   | Email address for the staff to access the system.         | Vendor                   |
| Password                | Staff's login password. (Stored securely)                 | Staff/Vendor             |
| Phone Number            | Contact phone number of the staff member.                 | Vendor                   |
| Is Active               | Indicates if the staff member is currently active or not. | Vendor                   |
| Created Date            | Date when the staff profile was created. (Generated Automatically) | System                   |

```

```
Staff Schedule

| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Appointment ID          | Links to the specific appointment assigned to the staff member. | System                   |
| Staff ID                | Links to the staff member’s profile.                      | System                   |
| Vendor ID               | Links to the vendor’s profile.                            | System                   |
| Customer ID             | Links to the customer who booked the appointment.         | System                   |
| Service ID              | The service provided by the staff member during the appointment. | System                   |
| Appointment Date        | Date and time of the appointment.                         | Vendor/Customer          |
| Status                  | Status of the appointment (e.g., confirmed, completed, canceled). | Vendor/System            |
```

```
Staff Performance Metrics

| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Metric ID               | A unique identifier for each performance entry. (Generated Automatically) | System                   |
| Staff ID                | Links to the staff member’s profile.                      | System                   |
| Vendor ID               | Links to the vendor.                                      | System                   |
| Appointments Completed  | The total number of appointments completed by the staff member. (Generated Automatically) | System                   |
| Average Customer Rating | The average rating given by customers after appointments. (Generated Automatically) | System                   |
| Feedback/Notes          | Notes or feedback the staff leaves after completing appointments. (Optional) | Staff                    |
| Report Generated Date   | Date when the performance metrics were last updated. (Generated Automatically) | System                   |

```

```
Staff Payroll

| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Payroll ID              | A unique identifier for each payroll record. (Generated Automatically) | System                   |
| Staff ID                | Links to the staff member’s profile.                      | System                   |
| Vendor ID               | Links to the vendor.                                      | System                   |
| Hours Worked            | Total hours worked by the staff member for a specific period. (Generated Automatically) | System                   |
| Appointments Completed  | Number of completed appointments used for payroll calculations. (Generated Automatically) | System                   |
| Amount Paid             | Total amount paid to the staff member for the work period. (Generated Automatically) | System                   |
| Payment Date            | Date when the payment was processed. (Generated Automatically) | System                   |
```

## **Marketing Content Manager Component**
```
List of table will have for Marketing Content Manager:
1. Website Maintainer Table
2. Website Content Table
3. Promotions and Marketing Campaigns Table
4. Analytics and Performance Reports Table
5. Social Media Integration Table
```

```
Website Maintainer Table

| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Maintainer ID           | A unique identifier for each website maintainer or marketing content manager. (Generated Automatically) | System                   |
| First Name              | First name of the website maintainer.                     | Maintainer               |
| Last Name               | Last name of the website maintainer.                      | Maintainer               |
| Email                   | Email address for login and communication.                | Maintainer               |
| Password                | Password chosen for login. (Stored securely)              | Maintainer               |
| Role                    | The role or designation (e.g., content editor, marketing manager). | Admin                    |
| Phone Number            | Contact number for communication. (Optional)             | Maintainer               |
| Created Date            | The date when the profile was created. (Generated Automatically) | System                   |
| Last Updated            | The last time the profile was updated. (Generated Automatically) | System                   |
| Is Active               | Indicates if the maintainer is active or inactive in the system. | System/Admin             |

```

```
Website Content Table

| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Content ID              | A unique identifier for each piece of content. (Generated Automatically) | System                   |
| Maintainer ID           | Links to the website maintainer responsible for the content. | System                   |
| Title                   | The title of the content (e.g., blog post, promotion title). | Maintainer               |
| Body                    | The main content, which can include HTML, text, or formatted content. | Maintainer               |
| Category                | Category of content (e.g., blog, promotion, update).       | Maintainer               |
| Created Date            | Date the content was created. (Generated Automatically)    | System                   |
| Last Updated            | Date the content was last updated. (Generated Automatically) | System                   |
| Is Published            | Indicates if the content is published or still in draft form. | Maintainer               |

```


```
Promotions and Marketing Campaigns Table
| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Campaign ID             | A unique identifier for each marketing campaign or promotion. (Generated Automatically) | System                   |
| Maintainer ID           | Links to the maintainer responsible for managing the campaign. | System                   |
| Campaign Title          | Title or name of the campaign or promotion.                | Maintainer               |
| Description             | Details about the promotion or campaign.                   | Maintainer               |
| Start Date              | The start date for the campaign or promotion.              | Maintainer               |
| End Date                | The end date for the campaign or promotion.                | Maintainer               |
| Discount Code           | Discount or promotional code associated with the campaign. (Optional) | Maintainer               |
| Target Audience         | The target audience for the campaign (e.g., new customers, repeat customers). (Optional) | Maintainer               |
| Status                  | Indicates if the campaign is active, paused, or completed. | Maintainer               |

```


```
Analytics and Performance Reports Table
| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Report ID               | A unique identifier for each report. (Generated Automatically) | System                   |
| Maintainer ID           | Links to the maintainer who generated the report.          | System                   |
| Report Type             | Type of report (e.g., website traffic, campaign performance). | Maintainer               |
| Start Date              | The start date for the period being analyzed.              | Maintainer               |
| End Date                | The end date for the period being analyzed.                | Maintainer               |
| Report Data             | Data collected and generated automatically by the system (e.g., views, clicks, conversions). | System                   |
| Generated Date          | The date the report was created or generated. (Generated Automatically) | System                   |

```


```
Social Media Integration Table
| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Integration ID          | A unique identifier for each social media integration. (Generated Automatically) | System                   |
| Maintainer ID           | Links to the maintainer managing the integration.          | System                   |
| Platform Name           | Name of the social media platform (e.g., Facebook, Instagram). | Maintainer               |
| Account Username/ID     | The username or ID of the connected account.               | Maintainer               |
| API Key/Token           | API keys or tokens used for integrating the platform.      | Maintainer               |
| Last Synced Date        | The last date when the system synced with the social media platform. (Generated Automatically) | System                   |
```


## *System Administrator Component**
```
List of table will have for System Administrator:
1. System Administrator Table
2. User Management Table
3. System Configuration Table
4. Security Logs Table
5.  Audit Logs Table
6. Payment Gateway Management Table
7. System Notifications Table
```

```
 System Administrator Table

| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Admin ID                | A unique identifier for each system administrator. (Generated Automatically) | System                   |
| First Name              | First name of the system administrator.                   | Admin                    |
| Last Name               | Last name of the system administrator.                    | Admin                    |
| Email                   | Email address for login and communication.                | Admin                    |
| Password                | Password for login. (Stored securely)                     | Admin                    |
| Role                    | Admin role type (e.g., Super Admin, Support Admin).       | Admin/System             |
| Phone Number            | Contact number for communication. (Optional)             | Admin                    |
| Created Date            | Date when the admin account was created. (Generated Automatically) | System                   |
| Last Updated            | Date of the last update to the admin profile. (Generated Automatically) | System                   |
| Is Active               | Indicates if the admin account is active or deactivated.  | System                   |

```

```
User Management Table

| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Management ID           | A unique identifier for each user management action. (Generated Automatically) | System                   |
| Admin ID                | Links to the system administrator who performed the action. | System                   |
| User ID                 | Links to the user (customer, vendor, staff) whose data is being managed. | System                   |
| Action Type             | The type of action performed (e.g., create, delete, update). | Admin                    |
| Action Details          | Description or notes about the action. (Optional)         | Admin                    |
| Action Date             | The date the action was performed. (Generated Automatically) | System                   |

```

```
System Configuration Table

| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Config ID               | A unique identifier for each system configuration entry. (Generated Automatically) | System                   |
| Admin ID                | Links to the admin making the configuration change.       | System                   |
| Setting Name            | The name of the configuration setting (e.g., "Max Login Attempts"). | Admin                    |
| Setting Value           | The value of the setting (e.g., "5 attempts").            | Admin                    |
| Updated Date            | The date when the setting was updated. (Generated Automatically) | System                   |


```


```
Security Logs Table

| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Log ID                  | A unique identifier for each security log. (Generated Automatically) | System                   |
| Admin ID                | Links to the admin who generated the log or managed the event. | System                   |
| Event Type              | The type of security event (e.g., login attempt, password reset). (Generated Automatically) | System                   |
| IP Address              | The IP address of the user or admin performing the action. (Generated Automatically) | System                   |
| Timestamp               | The time when the event occurred. (Generated Automatically) | System                   |
| Event Status            | Status of the event (e.g., success, failure). (Generated Automatically) | System                   |

```

```
 Audit Logs Table


| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Audit Log ID            | A unique identifier for each audit log entry. (Generated Automatically) | System                   |
| Admin ID                | Links to the admin responsible for the action.            | System                   |
| Action Description      | A description of the action performed (e.g., “Deleted User Profile”). | Admin/System             |
| Affected Entity         | The entity affected by the action (e.g., customer, vendor, service). (Generated Automatically) | System                   |
| Timestamp               | The time the action was performed. (Generated Automatically) | System                   |
| Status                  | Status of the action (e.g., successful, failed). (Generated Automatically) | System                   |

```

```
Payment Gateway Management Table
| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Gateway ID              | A unique identifier for each payment gateway configuration. (Generated Automatically) | System                   |
| Admin ID                | Links to the admin who configured or updated the gateway. | System                   |
| Gateway Name            | Name of the payment gateway (e.g., PayPal, Stripe).       | Admin                    |
| API Key/Token           | API key or token for integrating with the payment gateway. | Admin                    |
| Is Active               | Indicates if the payment gateway is active or inactive.   | Admin                    |
| Last Updated            | The date the gateway was last updated. (Generated Automatically) | System                   |


```

```
System Notifications Table

| **Field Name**          | **Description**                                           | **Filled By**            |
|-------------------------|-----------------------------------------------------------|--------------------------|
| Notification ID         | A unique identifier for each notification sent. (Generated Automatically) | System                   |
| Admin ID                | Links to the admin who managed or triggered the notification. | System                   |
| Notification Type       | Type of notification (e.g., system update, payment alert). | Admin/System             |
| Message                 | The content of the notification message.                  | Admin                    |
| Recipient               | The recipient(s) of the notification (e.g., all users, specific users). | Admin/System             |
| Sent Date               | The date the notification was sent. (Generated Automatically) | System                   |

```