from datetime import datetime, timedelta, timezone
from opentelemetry import trace
import logging
from lib.db import pool 

tracer = trace.get_tracer("home.activities")

class HomeActivities:
  def run():
    #logger.info("homeactivities")
    with tracer.start_as_current_span("home-activities-mock-data"):
      span = trace.get_current_span()
      now = datetime.now(timezone.utc).astimezone()

      span.set_attribute("app.now", now.isoformat())
      
      
      sql = query_wrap_array("""
      SELECT
        activities.uuid,
        users.display_name,
        users.handle,
        activities.message,
        activities.replies_count,
        activities.reposts_count,
        activities.likes_count,
        activities.reply_to_activity_uuid,
        activities.expires_at,
        activities.created_at
      FROM public.activities
      LEFT JOIN public.users ON users.uuid = activities.user_uuid
      ORDER BY activities.created_at DESC
      """)
      print(sql)
      with pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(sql)
          # this will return a tuple
          # the first field being the data
          # https://www.psycopg.org/psycopg3/docs/api/cursors.html#psycopg.Cursor.fetchone
          json = cur.fetchone()
      return json[0]
      span.set_attribute("app.result_length", len(results))
      return results