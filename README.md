# GoogleSearch-API
Fetches article titles, images and links or research paper title, description and link for an entered search term

## Usage

```
https://dac-api.herokuapp.com/news
https://dac-api.herokuapp.com/papers
```

## Request news for a specific topic

```
?topic="{topic}"
```

## Output format

### News

```
{
  title,
  image,
  link
}
```

### Research Papers

```
{
  desc,
  link,
  title,
}
```

### Blogs

```
{
  img,
  link,
  readtime,
  title
}
```