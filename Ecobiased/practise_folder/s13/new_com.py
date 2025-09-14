input_data = {

  "candidate_id": "CAND_001",
  "personal_info": {
    "name": "John Smith",
    "email": "john.smith@email.com",
    "phone": "+1-555-123-4567",
    "location": "San Francisco, CA"
  },
  "work_experience": [
    {
      "id": "exp_001",
      "company_name": "TechCorp Inc.",
      "position": "Senior Software Engineer",
      "start_date": "2022-03-15",
      "end_date": "2024-01-20",
      "is_current": False,
      "location": "San Francisco, CA",
      "employment_type": "Full-time",
      "industry": "Technology",
      "department": "Engineering",
      "salary_range": {
        "start": 120000,
        "end": 150000,
        "currency": "USD"
      },
      "responsibilities": [
        "Led development of microservices architecture for e-commerce platform",
        "Mentored junior developers and conducted code reviews",
        "Collaborated with product managers to define technical requirements",
        "Implemented CI/CD pipelines using Jenkins and Docker"
      ],
      "achievements": [
        "Reduced API response time by 40% through optimization",
        "Successfully delivered 3 major features ahead of schedule",
        "Improved code coverage from 65% to 85%"
      ],
      "technologies": [
        "Python", "Django", "React", "PostgreSQL", "AWS", "Docker"
      ],
      "reports_to": "Engineering Manager",
      "team_size": 8,
      "reason_for_leaving": "Career growth opportunity"
    },
    {
      "id": "exp_002",
      "company_name": "StartupXYZ",
      "position": "Software Engineer",
      "start_date": "2020-06-01",
      "end_date": "2022-03-01",
      "is_current": False,
      "location": "Austin, TX",
      "employment_type": "Full-time",
      "industry": "SaaS",
      "department": "Product Development",
      "salary_range": {
        "start": 85000,
        "end": 100000,
        "currency": "USD"
      },
      "responsibilities": [
        "Developed RESTful APIs using Node.js and Express",
        "Built responsive web applications with React and TypeScript",
        "Worked with MongoDB and Redis for data storage",
        "Participated in agile development processes"
      ],
      "achievements": [
        "Built customer dashboard that increased user engagement by 25%",
        "Reduced bug reports by 30% through improved testing practices"
      ],
      "technologies": [
        "JavaScript", "Node.js", "React", "TypeScript", "MongoDB", "Redis"
      ],
      "reports_to": "Lead Developer",
      "team_size": 5,
      "reason_for_leaving": "Company acquisition"
    }
  ],
  "total_experience_years": 3.5,
  "skills_summary": {
    "programming_languages": ["Python", "JavaScript", "TypeScript"],
    "frameworks": ["Django", "React", "Node.js", "Express"],
    "databases": ["PostgreSQL", "MongoDB", "Redis"],
    "cloud_platforms": ["AWS", "Docker"],
    "soft_skills": ["Leadership", "Mentoring", "Problem Solving", "Communication"]
  },
  "career_objectives": [
    "Lead technical teams in building scalable applications",
    "Contribute to open-source projects",
    "Stay updated with emerging technologies"
  ],
  "references": [
    {
      "name": "Jane Doe",
      "position": "Engineering Manager",
      "company": "TechCorp Inc.",
      "email": "jane.doe@techcorp.com",
      "phone": "+1-555-987-6543"
    }
  ]
}
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def calculate_total_experience(work_experience):
    # 1. Convert start and end dates to datetime and build ranges
    ranges = []
    for exp in work_experience:
        start = datetime.strptime(exp['start_date'], '%Y-%m-%d')
        end = datetime.strptime(exp['end_date'], '%Y-%m-%d') if not exp['is_current'] else datetime.today()
        ranges.append((start, end))

    # 2. Sort ranges by start date
    ranges.sort(key=lambda x: x[0])

    # 3. Merge overlapping or adjacent ranges
    merged_ranges = []
    for start, end in ranges:
        if not merged_ranges:
            merged_ranges.append((start, end))
        else:
            last_start, last_end = merged_ranges[-1]
            if start <= last_end + timedelta(days=1):  # overlapping or adjacent
                merged_ranges[-1] = (last_start, max(last_end, end))
            else:
                merged_ranges.append((start, end))

    # 4. Calculate total duration in days
    total_days = sum((end - start).days + 1 for start, end in merged_ranges)

    # 5. Convert days to years, months, days using relativedelta
    base_date = datetime(2000, 1, 1)
    final_date = base_date + timedelta(days=total_days)
    delta = relativedelta(final_date, base_date)

    return {
        "years": delta.years,
        "months": delta.months,
        "days": delta.days
    }

# Example usage
result = calculate_total_experience(input_data['work_experience'])
print("Total Experience:", result)

from datetime import datetime, timedelta


def calculate_total_experience(work_experience):

  ranges = []

  for exp in work_experience:
      start = datetime.strptime(exp['start'], '%y-%m-%d')
      end = datetime.strptime(exp['end'], '%y-%m-%d') if not exp['is_current'] else datetime.today()
      ranges.append((start, end))

  ranges.sort(key=lambda x:x[0])

  merged = []
  for start, end in ranges:
      if not merged:
          merged.append((start, end))
      else:
          last_start, last_end = merged[-1]
          if start <= last_end + timedelta(days=1):
              merged[-1] = (last_start, max(last_end, end))
          else:
              merged.append((start, end))
  total_sum_of_days = sum((end - start).days + 1 for start, end in merged)

  base_date = datetime(2000, 1, 1)
  final_date = base_date + timedelta(days=total_sum_of_days)
  delta = relativedelta(final_date - base_date)
  return {
    "years": delta.years,
    "months": delta.months,
    "days": delta.days
  }

result = calculate_total_experience(input_data['work_experience'])
print("Total Experience:", result)
