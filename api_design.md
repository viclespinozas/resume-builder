# REST API Design for Resume Builder Application

## Overview
This document outlines the REST API endpoints for the resume builder application. The API follows a clean architecture approach using FastAPI with proper authentication, validation, and error handling.

## Authentication
All endpoints (except login/register) require JWT authentication via Authorization header:
```
Authorization: Bearer <jwt_token>
```

## Base URL
`/api/v1`

## Endpoints

### 1. Authentication
**POST /auth/register**
- Description: Register a new user
- Request Body:
```json
{
  "email": "string",
  "password": "string"
}
```
- Response: 
```json
{
  "access_token": "string",
  "token_type": "bearer"
}
```

**POST /auth/login**
- Description: Login user and get JWT token
- Request Body:
```json
{
  "email": "string",
  "password": "string"
}
```
- Response:
```json
{
  "access_token": "string",
  "token_type": "bearer"
}
```

### 2. Users
**GET /users/me**
- Description: Get current user profile
- Response:
```json
{
  "id": "uuid",
  "email": "string",
  "created_at": "datetime",
  "updated_at": "datetime",
  "is_active": "boolean",
  "profile": {
    "id": "uuid",
    "user_id": "uuid",
    "first_name": "string",
    "last_name": "string",
    "title": "string",
    "location": "string",
    "phone": "string",
    "email": "string",
    "linkedin_url": "string",
    "github_url": "string",
    "summary": "string",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
}
```

**PUT /users/me**
- Description: Update current user profile
- Request Body:
```json
{
  "first_name": "string",
  "last_name": "string",
  "title": "string",
  "location": "string",
  "phone": "string",
  "email": "string",
  "linkedin_url": "string",
  "github_url": "string",
  "summary": "string"
}
```
- Response: Updated user profile object

### 3. Resumes
**GET /resumes**
- Description: Get all resumes for current user
- Response:
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "title": "string",
    "template_id": "uuid",
    "is_active": "boolean",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
]
```

**POST /resumes**
- Description: Create a new resume
- Request Body:
```json
{
  "title": "string",
  "template_id": "uuid"
}
```
- Response:
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "title": "string",
  "template_id": "uuid",
  "is_active": "boolean",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**GET /resumes/{resume_id}**
- Description: Get a specific resume
- Response:
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "title": "string",
  "template_id": "uuid",
  "is_active": "boolean",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**PUT /resumes/{resume_id}**
- Description: Update a resume
- Request Body:
```json
{
  "title": "string",
  "template_id": "uuid"
}
```
- Response: Updated resume object

**DELETE /resumes/{resume_id}**
- Description: Delete a resume

### 4. Resume Versions
**GET /resumes/{resume_id}/versions**
- Description: Get all versions of a resume
- Response:
```json
[
  {
    "id": "uuid",
    "resume_id": "uuid",
    "version_number": "integer",
    "content": "jsonb",
    "created_at": "datetime",
    "is_current": "boolean"
  }
]
```

**GET /resumes/{resume_id}/versions/{version_id}**
- Description: Get a specific version of a resume
- Response:
```json
{
  "id": "uuid",
  "resume_id": "uuid",
  "version_number": "integer",
  "content": "jsonb",
  "created_at": "datetime",
  "is_current": "boolean"
}
```

**POST /resumes/{resume_id}/versions**
- Description: Create a new version of a resume
- Request Body:
```json
{
  "content": "jsonb"
}
```
- Response:
```json
{
  "id": "uuid",
  "resume_id": "uuid",
  "version_number": "integer",
  "content": "jsonb",
  "created_at": "datetime",
  "is_current": "boolean"
}
```

### 5. Templates
**GET /templates**
- Description: Get all available templates
- Response:
```json
[
  {
    "id": "uuid",
    "name": "string",
    "description": "string",
    "content": "jsonb",
    "is_active": "boolean",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
]
```

**GET /templates/{template_id}**
- Description: Get a specific template
- Response:
```json
{
  "id": "uuid",
  "name": "string",
  "description": "string",
  "content": "jsonb",
  "is_active": "boolean",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**POST /templates**
- Description: Create a new template
- Request Body:
```json
{
  "name": "string",
  "description": "string",
  "content": "jsonb"
}
```
- Response:
```json
{
  "id": "uuid",
  "name": "string",
  "description": "string",
  "content": "jsonb",
  "is_active": "boolean",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**PUT /templates/{template_id}**
- Description: Update a template
- Request Body:
```json
{
  "name": "string",
  "description": "string",
  "content": "jsonb"
}
```
- Response: Updated template object

**DELETE /templates/{template_id}**
- Description: Delete a template

### 6. Uploaded Files
**GET /files**
- Description: Get all uploaded files for current user
- Response:
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "filename": "string",
    "file_path": "string",
    "file_type": "string",
    "size": "integer",
    "created_at": "datetime"
  }
]
```

**POST /files/upload**
- Description: Upload a new file
- Request Body: Form data with file upload
- Response:
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "filename": "string",
  "file_path": "string",
  "file_type": "string",
  "size": "integer",
  "created_at": "datetime"
}
```

**GET /files/{file_id}**
- Description: Get a specific uploaded file
- Response:
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "filename": "string",
  "file_path": "string",
  "file_type": "string",
  "size": "integer",
  "created_at": "datetime"
}
```

**DELETE /files/{file_id}**
- Description: Delete an uploaded file

### 7. Job Descriptions
**GET /job-descriptions**
- Description: Get all job descriptions for current user
- Response:
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "title": "string",
    "company": "string",
    "location": "string",
    "description": "string",
    "requirements": "jsonb",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
]
```

**POST /job-descriptions**
- Description: Create a new job description
- Request Body:
```json
{
  "title": "string",
  "company": "string",
  "location": "string",
  "description": "string",
  "requirements": "jsonb"
}
```
- Response:
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "title": "string",
  "company": "string",
  "location": "string",
  "description": "string",
  "requirements": "jsonb",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**GET /job-descriptions/{job_id}**
- Description: Get a specific job description
- Response:
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "title": "string",
  "company": "string",
  "location": "string",
  "description": "string",
  "requirements": "jsonb",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**PUT /job-descriptions/{job_id}**
- Description: Update a job description
- Request Body:
```json
{
  "title": "string",
  "company": "string",
  "location": "string",
  "description": "string",
  "requirements": "jsonb"
}
```
- Response: Updated job description object

**DELETE /job-descriptions/{job_id}**
- Description: Delete a job description

### 8. AI Requests
**GET /ai-requests**
- Description: Get all AI requests for current user
- Response:
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "prompt": "string",
    "response": "string",
    "model_used": "string",
    "status": "string",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
]
```

**POST /ai-requests**
- Description: Send a request to AI
- Request Body:
```json
{
  "prompt": "string",
  "model_used": "string"
}
```
- Response:
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "prompt": "string",
  "response": "string",
  "model_used": "string",
  "status": "string",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**GET /ai-requests/{request_id}**
- Description: Get a specific AI request
- Response:
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "prompt": "string",
  "response": "string",
  "model_used": "string",
  "status": "string",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### 9. Exports
**GET /exports**
- Description: Get all exports for current user
- Response:
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "resume_id": "uuid",
    "export_format": "string",
    "file_path": "string",
    "created_at": "datetime"
  }
]
```

**POST /exports**
- Description: Export a resume
- Request Body:
```json
{
  "resume_id": "uuid",
  "export_format": "string"
}
```
- Response:
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "resume_id": "uuid",
  "export_format": "string",
  "file_path": "string",
  "created_at": "datetime"
}
```

**GET /exports/{export_id}**
- Description: Get a specific export
- Response:
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "resume_id": "uuid",
  "export_format": "string",
  "file_path": "string",
  "created_at": "datetime"
}
```

### 10. Settings
**GET /settings**
- Description: Get all settings for current user
- Response:
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "key": "string",
    "value": "string",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
]
```

**GET /settings/{setting_key}**
- Description: Get a specific setting
- Response:
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "key": "string",
  "value": "string",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

**POST /settings**
- Description: Create or update a setting
- Request Body:
```json
{
  "key": "string",
  "value": "string"
}
```
- Response:
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "key": "string",
  "value": "string",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

## Error Responses

All error responses follow this format:
```json
{
  "error": {
    "code": "string",
    "message": "string",
    "details": "object"
  }
}
```

Common error codes:
- `UNAUTHORIZED`: Authentication required or invalid token
- `FORBIDDEN`: Insufficient permissions
- `NOT_FOUND`: Resource not found
- `VALIDATION_ERROR`: Invalid input data
- `INTERNAL_SERVER_ERROR`: Server-side error

## Rate Limiting
API endpoints are subject to rate limiting (default: 100 requests per hour per user).