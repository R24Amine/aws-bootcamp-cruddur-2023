# Week 2 — Distributed Tracing

## What is the distributed tracing ?

A program is something that you can run and test on your software and a software is another thing bigger, that is probably running in the cloud that connects to other software and actual people but they are harder to track because it is not deterministic (there is file systems that get full, network disconnection, othher dependencies etc...) that makes more requests to handle, so for programs there is a debugger and for softwares there is observability, and the Software gets really complicated and goes bigger and bigger, that is why we always need to know what is going on.

In the past we have logs for our programs in a file log, but when we get a lot of services happening a bunch of separated log lines cannot trace it, so we need a story of what happened, that is what we call distributed tracing, as the request goes to different systems we can get more information (especially for the backend), and that is what we call modern observability.

## Instrumentation using Honeycomb

The goal is to have Spans, which are part of a trace, it has a start time and a duration, represents a single unit of work, and you can see what is happening exactly in more details (for example what SQl query is executing in the database).

Therefore traces tell you what happened and when it happened at the same time. as your system building is going bigger these traces will help you understand what is going on (you can see how long a database queries happened, you can see where an error happened and what service and how we get to that service).

We can also have service map for visual tracing but this feature is not free!

Instrumentation is the code that sends the data to make these traces.

That is why we will try to use Honeycomb because it is easier for observability (loging, tracing..), in a second part we will try AWS X-ray service which is more harder to implement but very useful.

