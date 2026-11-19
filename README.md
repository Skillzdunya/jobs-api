# SkillzDunya Jobs API

Free, read-only JSON API for **government and private jobs in Pakistan**, from
[SkillzDunya](https://skillzdunya.com).

- No API key, no sign-up
- HTTPS, CORS-friendly JSON
- Rate limit: 60 requests per minute per IP
- Data updated daily; every government ad is checked against its official source

**Base URL:** `https://skillzdunya.com/api/v1`
**OpenAPI 3.1:** https://skillzdunya.com/api/v1/openapi.json
**Self-describing index:** https://skillzdunya.com/api/v1

## Endpoints

| Method | Path | What it returns |
|---|---|---|
| GET | `/api/v1/jobs` | Paginated, filterable job list |
| GET | `/api/v1/jobs/{slug}` | One job in full: every post with its BPS grade, age limit, experience, qualifications and cities, plus FAQs and how to apply |
| GET | `/api/v1/facets` | Every accepted filter value (city, province, organization, category, qualification, testing agency) with live open-vacancy counts |

### Filters for `/api/v1/jobs`

| Parameter | Example | Notes |
|---|---|---|
| `q` | `q=lecturer` | Free-text search |
| `city` | `city=lahore` | Slug from `/facets` |
| `province` | `province=punjab` | Slug from `/facets` |
| `organization` | `organization=fpsc` | Slug from `/facets` |
| `category` | `category=private-jobs` | Slug from `/facets` |
| `qualification` | `qualification=bsc` | Slug from `/facets` |
| `testing_agency` | `testing_agency=nts` | Slug from `/facets` |
| `gender` | `gender=female` | |
| `government` | `government=1` | `1` = government only, `0` = private only |
| `international` | `international=1` | Overseas jobs |
| `bps_min`, `bps_max` | `bps_min=16&status=all` | Pay scale range |
| `salary_min` | `salary_min=100000` | PKR per month |
| `experience_max` | `experience_max=0` | Years; `0` = fresh graduates |
| `status` | `status=open` | `open`, `expired` or `all` |
| `posted_since` | `posted_since=2026-11-01` | Date |
| `sort` | `sort=deadline` | `newest`, `deadline` or `popular` |
| `per_page` | `per_page=50` | Page size |

## Examples

Government jobs in Lahore for BSc graduates with no experience:

```bash
curl "https://skillzdunya.com/api/v1/jobs?city=lahore&qualification=bsc&government=1&experience_max=0"
```

Private jobs posted this month:

```bash
curl "https://skillzdunya.com/api/v1/jobs?government=0&posted_since=2026-11-01"
```

One job in full:

```bash
curl "https://skillzdunya.com/api/v1/jobs/{slug}"
```

More in [`examples/`](examples/) (Python and JavaScript).

## Response (shortened)

```json
{
  "data": [
    {
      "slug": "uet-lahore-jobs-2026",
      "title": "UET Lahore Jobs 2026",
      "url": "https://skillzdunya.com/job/uet-lahore-jobs-2026",
      "organization": { "title": "...", "slug": "..." },
      "is_government": true,
      "published_at": "2026-11-19",
      "deadline": "2026-12-05",
      "is_expired": false,
      "total_vacancies": 12
    }
  ]
}
```

## Attribution

Free to use. Each record has a `url` field with the job's page on SkillzDunya: please link to
that page when you show the job. For anything heavier than the rate limit allows, write to
info@skillzdunya.com.

This repository holds documentation and examples only; the API is served by skillzdunya.com.
