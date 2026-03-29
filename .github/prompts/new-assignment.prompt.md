---
description: "Create a new programming homework assignment"
agent: "agent"
argument-hint: "Provide assignment details"
---

# Create New Programming Assignment

Your goal is to generate a new homework assignment for Mergington High School students.

## Step 1: Gather Assignment Information

If details are not already provided, ask what the assignment should be about.

## Step 2: Create Assignment Structure

1. Create a new directory in [assignments](../../assignments/) with a unique name based on the assignment topic.
2. Create a [README.md](../../templates/assignment-template.md) in that directory using the structure from [assignment-template.md](../../templates/assignment-template.md).
3. Fill out the assignment details in the README file.
4. Optionally add starter code or attachments to the same assignment folder when needed.

## Step 3: Update Website Configuration

Update [config.json](../../config.json) to include the new assignment.

For `dueDate`, use the current date plus 7 days unless the user specifies another due date.
