# SPEC-001: GoWabi Clone MVP

## Background

This project aims to build a minimal viable product (MVP) for a spa-salon booking and management system similar to GoWabi. The MVP focuses on service search and booking, vendor management, user management, payment integration, and an admin panel for system control.

## Requirements

The MVP functionalities are scoped as follows:

### Must Have:
- Service search and booking (category, price, rating, and location).
- Vendor management for service listings and booking views.
- User management for personal profiles and booking history.
- Basic online payment (credit card or PayPal).
- Admin panel for managing vendors, users, and bookings.

### Should Have:
- A responsive design using Bootstrap5.

### Won’t Have (For Now):
- Advanced analytics or reporting.
- Loyalty programs or complex promotions.

## Method

### High-Level Architecture

The architecture will follow a modular design using Django for the backend and Bootstrap5 for the frontend. SQLite will be used as the database for development simplicity.

### Database Design

Here’s a relational schema overview:

- **User Table**
  - Fields: `id`, `username`, `email`, `password`, `date_joined`, `last_login`
  - Relationships: `user` has a one-to-many relationship with `Bookings`.

- **Vendor Table**
  - Fields: `id`, `name`, `address`, `contact_info`
  - Relationships: `vendor` has a one-to-many relationship with `Services`.

- **Service Table**
  - Fields: `id`, `name`, `category`, `price`, `duration`, `vendor_id`
  - Relationships: Each `service` belongs to one `vendor`.

- **Booking Table**
  - Fields: `id`, `user_id`, `service_id`, `booking_date`, `status`
  - Relationships: `booking` links a `user` and a `service`.

- **Admin Table**
  - Fields: `id`, `username`, `password`

### Component Overview

#### Frontend:
- **Pages**: Home, Service Listings, Service Detail, Vendor Dashboard, User Profile, Admin Panel.
- **Framework**: Bootstrap5 for styling and responsive design.

#### Backend:
- **Framework**: Django.
- **Core Modules**:
  - User Authentication
  - Vendor and Service Management
  - Booking System
  - Payment Integration

#### Database:
- SQLite with tables for users, vendors, services, and bookings.

#### Deployment:
- Local development server with Django's built-in server.

## Milestones

- **Milestone 1**: Complete database schema and Django models.
- **Milestone 2**: Implement core views and templates (Home, Search, Service Detail, Booking).
- **Milestone 3**: Add Vendor and Admin dashboards.
- **Milestone 4**: Integrate payment gateway (mock for local use).

## Gathering Results

Evaluation will be based on:
1. Successful booking flow for users.
2. Vendor ability to manage services and view bookings.
3. Admin control over user and vendor data.
4. Payment flow simulation and database updates.
