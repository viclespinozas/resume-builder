# Database Design for Resume Builder Application

## ER Diagram (Text)

```
┌─────────────┐    ┌──────────────┐    ┌────────────────┐
│   Users     │◄───┤  Profiles    │◄───┤  Resumes       │
└─────────────┘    └──────────────┘    └────────────────┘
        │                   │                │
        │                   │                │
        ▼                   ▼                ▼
┌────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│ Resume Versions│   │ Templates       │   │ Resume History  │
└────────────────┘   └─────────────────┘   └─────────────────┘
        │                   │                │
        │                   │                │
        ▼                   ▼                ▼
┌────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│ Uploaded Files │   │ Job Descriptions│   │ AI Requests     │
└────────────────┘   └─────────────────┘   └─────────────────┘
        │                   │                │
        │                   │                │
        ▼                   ▼                ▼
┌────────────────┐   ┌─────────────────┐   ┌─────────────────┐
│ Exports        │   │ Settings        │   │                 │
└────────────────┘   └─────────────────┘   └─────────────────┘
```

## Tables

### 1. Users
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier for user |
| email | VARCHAR(255) | UNIQUE, NOT NULL | User's email address |
| password_hash | VARCHAR(255) | NOT NULL | Hashed password |
| created_at | TIMESTAMP | DEFAULT NOW() | When user was created |
| updated_at | TIMESTAMP | DEFAULT NOW() | When user was last updated |
| is_active | BOOLEAN | DEFAULT TRUE | Whether user account is active |

### 2. Profiles
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier for profile |
| user_id | UUID | FOREIGN KEY (Users.id), NOT NULL | Reference to user |
| first_name | VARCHAR(100) | NOT NULL | User's first name |
| last_name | VARCHAR(100) | NOT NULL | User's last name |
| title | VARCHAR(255) |  | Professional title |
| location | VARCHAR(255) |  | Location information |
| phone | VARCHAR(50) |  | Phone number |
| email | VARCHAR(255) |  | Email address |
| linkedin_url | VARCHAR(255) |  | LinkedIn profile URL |
| github_url | VARCHAR(255) |  | GitHub profile URL |
| summary | TEXT |  | Professional summary |
| created_at | TIMESTAMP | DEFAULT NOW() | When profile was created |
| updated_at | TIMESTAMP | DEFAULT NOW() | When profile was last updated |

### 3. Resumes
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier for resume |
| user_id | UUID | FOREIGN KEY (Users.id), NOT NULL | Reference to user |
| title | VARCHAR(255) | NOT NULL | Resume title |
| template_id | UUID | FOREIGN KEY (Templates.id) | Reference to template used |
| is_active | BOOLEAN | DEFAULT TRUE | Whether this resume is active |
| created_at | TIMESTAMP | DEFAULT NOW() | When resume was created |
| updated_at | TIMESTAMP | DEFAULT NOW() | When resume was last updated |

### 4. Resume Versions
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier for version |
| resume_id | UUID | FOREIGN KEY (Resumes.id), NOT NULL | Reference to resume |
| version_number | INTEGER | NOT NULL | Version number |
| content | JSONB | NOT NULL | Resume content in JSON format |
| created_at | TIMESTAMP | DEFAULT NOW() | When version was created |
| is_current | BOOLEAN | DEFAULT FALSE | Whether this is the current version |

### 5. Templates
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier for template |
| name | VARCHAR(255) | NOT NULL | Template name |
| description | TEXT |  | Template description |
| content | JSONB | NOT NULL | Template structure in JSON format |
| is_active | BOOLEAN | DEFAULT TRUE | Whether template is active |
| created_at | TIMESTAMP | DEFAULT NOW() | When template was created |
| updated_at | TIMESTAMP | DEFAULT NOW() | When template was last updated |

### 6. Uploaded Files
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier for file |
| user_id | UUID | FOREIGN KEY (Users.id), NOT NULL | Reference to user |
| filename | VARCHAR(255) | NOT NULL | Original filename |
| file_path | VARCHAR(500) | NOT NULL | Path to stored file |
| file_type | VARCHAR(100) | NOT NULL | Type of file (e.g., 'pdf', 'docx') |
| size | INTEGER |  | File size in bytes |
| created_at | TIMESTAMP | DEFAULT NOW() | When file was uploaded |

### 7. Job Descriptions
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier for job description |
| user_id | UUID | FOREIGN KEY (Users.id), NOT NULL | Reference to user |
| title | VARCHAR(255) | NOT NULL | Job title |
| company | VARCHAR(255) |  | Company name |
| location | VARCHAR(255) |  | Job location |
| description | TEXT |  | Full job description |
| requirements | JSONB |  | Job requirements in JSON format |
| created_at | TIMESTAMP | DEFAULT NOW() | When job was added |
| updated_at | TIMESTAMP | DEFAULT NOW() | When job was last updated |

### 8. AI Requests
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier for AI request |
| user_id | UUID | FOREIGN KEY (Users.id), NOT NULL | Reference to user |
| prompt | TEXT | NOT NULL | The prompt sent to AI |
| response | TEXT |  | AI response |
| model_used | VARCHAR(100) |  | Name of the AI model used |
| status | VARCHAR(50) | DEFAULT 'pending' | Request status (pending, completed, failed) |
| created_at | TIMESTAMP | DEFAULT NOW() | When request was made |
| updated_at | TIMESTAMP | DEFAULT NOW() | When request was last updated |

### 9. Exports
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier for export |
| user_id | UUID | FOREIGN KEY (Users.id), NOT NULL | Reference to user |
| resume_id | UUID | FOREIGN KEY (Resumes.id) | Reference to resume |
| export_format | VARCHAR(50) | NOT NULL | Export format (pdf, docx, etc.) |
| file_path | VARCHAR(500) |  | Path to exported file |
| created_at | TIMESTAMP | DEFAULT NOW() | When export was created |

### 10. Settings
| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| id | UUID | PRIMARY KEY | Unique identifier for setting |
| user_id | UUID | FOREIGN KEY (Users.id), NOT NULL | Reference to user |
| key | VARCHAR(255) | NOT NULL | Setting key |
| value | TEXT |  | Setting value |
| created_at | TIMESTAMP | DEFAULT NOW() | When setting was created |
| updated_at | TIMESTAMP | DEFAULT NOW() | When setting was last updated |

## Indexes

### Users Table
- `idx_users_email` (email)
- `idx_users_created_at` (created_at)

### Profiles Table
- `idx_profiles_user_id` (user_id)
- `idx_profiles_created_at` (created_at)

### Resumes Table
- `idx_resumes_user_id` (user_id)
- `idx_resumes_template_id` (template_id)
- `idx_resumes_created_at` (created_at)

### Resume Versions Table
- `idx_resume_versions_resume_id` (resume_id)
- `idx_resume_versions_version_number` (version_number)
- `idx_resume_versions_created_at` (created_at)

### Templates Table
- `idx_templates_name` (name)
- `idx_templates_created_at` (created_at)

### Uploaded Files Table
- `idx_uploaded_files_user_id` (user_id)
- `idx_uploaded_files_created_at` (created_at)

### Job Descriptions Table
- `idx_job_descriptions_user_id` (user_id)
- `idx_job_descriptions_created_at` (created_at)

### AI Requests Table
- `idx_ai_requests_user_id` (user_id)
- `idx_ai_requests_status` (status)
- `idx_ai_requests_created_at` (created_at)

### Exports Table
- `idx_exports_user_id` (user_id)
- `idx_exports_resume_id` (resume_id)
- `idx_exports_created_at` (created_at)

### Settings Table
- `idx_settings_user_id` (user_id)
- `idx_settings_key` (key)
- `idx_settings_created_at` (created_at)

## Constraints

### Users Table
- Primary Key: id
- Unique Constraint: email

### Profiles Table
- Primary Key: id
- Foreign Key: user_id references Users(id) with ON DELETE CASCADE
- Not Null: first_name, last_name

### Resumes Table
- Primary Key: id
- Foreign Key: user_id references Users(id) with ON DELETE CASCADE
- Foreign Key: template_id references Templates(id) with ON DELETE SET NULL
- Not Null: title, user_id

### Resume Versions Table
- Primary Key: id
- Foreign Key: resume_id references Resumes(id) with ON DELETE CASCADE
- Not Null: resume_id, version_number, content

### Templates Table
- Primary Key: id
- Not Null: name, content

### Uploaded Files Table
- Primary Key: id
- Foreign Key: user_id references Users(id) with ON DELETE CASCADE
- Not Null: user_id, filename, file_path, file_type

### Job Descriptions Table
- Primary Key: id
- Foreign Key: user_id references Users(id) with ON DELETE CASCADE
- Not Null: title, user_id

### AI Requests Table
- Primary Key: id
- Foreign Key: user_id references Users(id) with ON DELETE CASCADE
- Not Null: prompt, user_id

### Exports Table
- Primary Key: id
- Foreign Key: user_id references Users(id) with ON DELETE CASCADE
- Foreign Key: resume_id references Resumes(id) with ON DELETE SET NULL
- Not Null: user_id, export_format

### Settings Table
- Primary Key: id
- Foreign Key: user_id references Users(id) with ON DELETE CASCADE
- Not Null: user_id, key

## Relationships Summary

1. **Users ↔ Profiles**: One-to-One (Each user has one profile)
2. **Users ↔ Resumes**: One-to-Many (Each user can have multiple resumes)
3. **Resumes ↔ Resume Versions**: One-to-Many (Each resume can have multiple versions)
4. **Users ↔ Uploaded Files**: One-to-Many (Each user can upload multiple files)
5. **Users ↔ Job Descriptions**: One-to-Many (Each user can have multiple job descriptions)
6. **Users ↔ AI Requests**: One-to-Many (Each user can make multiple AI requests)
7. **Users ↔ Exports**: One-to-Many (Each user can export multiple resumes)
8. **Users ↔ Settings**: One-to-Many (Each user can have multiple settings)
9. **Resumes ↔ Templates**: Many-to-One (Multiple resumes can use the same template)
10. **Resumes ↔ Exports**: One-to-Many (Each resume can be exported multiple times)

This design supports a comprehensive resume builder application with user management, resume creation and versioning, template support, file uploads, job descriptions, AI integration, export functionality, and user preferences.