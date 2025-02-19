# Django Leave Request application

## Introduction

Imagine you are a software developer at a company that values work-life balance and employee satisfaction. 
As part of this initiative, the company has decided to implement a new leave request management system. 
The goal of this system is to streamline the process of requesting and approving employee leave.
This application uses `Python 3` and Django `4.1`.


## Problem statement

1. Your task is to complete the implementation of its functionality using class-based views (`CBV`) and internationalization (`i18n`).
2. Make tests pass by implementing the missing features.
3. Be sure to complete all TODOs, but know not everything is explicitly tested.
4. Please do *NOT* modify any tests unless specifically told to do so.


### Task 1 - `leave/models.py`

* Use `leave.models.User` as a `User` model replacement for authentications.

### Task 2 - `leave/models.py`

* Modify the `LeaveRequest.request_ts` field to set it automatically when the object is created.
* Set human-readable singular (`user`) and plural (`users`) names for the `User` model. Make sure that the text translations remain in place.
* Add validation to the `LeaveRequest` model to ensure that the manager is different from the requesting user.

### Task 3 - `leave/admin.py`

* Register Django admin for `User` class.
* Show the language and manager columns in the list table.

### Task 4 - `leave/views.py`

#### `LeaveRequestList`

* Turn on pagination to display 20 items per page.
* Limit access to authenticated users only.

#### `LeaveRequestCreate`

* Please set `request_by` and `manager` using `Request` instance.
* Setup success redirect to `LeaveRequestDetail` view.

#### `LeaveRequestDetail`

* Validate the submitted value. If status is different then `accepted` or `rejected` then return an `HttpResponseBadRequest` with the text message `Please set correct status: {}`.
* Allow manager to review this request by `POST` submit `status`. Please set proper `LeaveRequest.review_ts` and `LeaveRequest.status` field.
* Return an `HttpResponseForbidden` if a non manager tries to `POST` a request.

#### `LeaveRequestUpdate`

* Redirect anonymous users to the login page.
* Upon successful update, redirect to the `LeaveRequestDetail` view.
* Raise `PermissionDenied` exception for users other than `LeaveRequest.request_by`.


## Hints

You shouldn't modify code outside the mentioned methods and the unit tests, just complete the specified features to make the unit tests run as expected.

To execute all unit tests, use:
```bash
pip install -q -e . && python3 setup.py pytest
```

