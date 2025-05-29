"""Basic connection example.
"""

import redis

r = redis.Redis(
    host='redis-16566.c278.us-east-1-4.ec2.redns.redis-cloud.com',
    port=16566,
    decode_responses=True,
    username="default",
    password="gKEDcsp2osQrzVI0BkDp3X4iD1yg0l9m",
)

success = r.set('foo', 'bar')
# True

result = r.get('foo')
print(result)
# >>> bar

