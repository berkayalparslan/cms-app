import { test, expect } from '@playwright/test';

test.use({storageState: '.auth/admin.json'})

test.describe('Posts CRUD', () => {
  test.beforeEach(async({page}) => {
    await page.goto('/');
  })
  test('Post - Create', async({page}) => {
    const post = {
      title: 'post title AT',
      content: 'post content AT'
    };
    const postTitleSlug = post.title.toLowerCase().replace(/\s/g,'-')
    const newPostButton = page.getByRole('link', {name: 'Add new post'});
    const postTitleInput = page.getByLabel('Title:');
    const postContentInput = page.getByLabel('Content:');
    const postSubmitButton = page.getByRole('button', {name: 'Submit'});
    const updatePostButton = page.getByRole('link', {name: 'Update post'});
    const deletePostButton = page.getByRole('button', {name: 'Delete post'});

    await newPostButton.click();
    await postSubmitButton.waitFor();
    await postTitleInput.fill(post.title);
    await postContentInput.fill(post.content);
    await postSubmitButton.click();

    await expect(page.url()).toContain(postTitleSlug);
    await expect(page.getByRole('heading',{level: 2, name: post.title })).toBeVisible();
    await expect(page.getByText(post.content)).toBeVisible();
    await expect(updatePostButton).toBeVisible();
    await expect(deletePostButton).toBeVisible();
    await expect(page.getByRole('heading',{level: 2, name: 'Comments' })).toBeVisible();
    await expect(page.getByText('No comments yet.')).toBeVisible();
  })
})