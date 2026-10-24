import time
import json
import urllib.request

req = urllib.request.Request(
    'http://192.168.128.59:7860/sdapi/v1/txt2img',
    data=json.dumps({
        'prompt': 'anime girl face, masterpiece, best quality',
        'negative_prompt': 'bad eyes, ugly',
        'width': 512,
        'height': 512,
        'steps': 12,
        'guidance_scale': 4.0,
        'sampler': 'Euler A Trailing'
    }).encode('utf-8'),
    headers={'Content-Type': 'application/json'}
)
t0 = time.time()
print('Starting test 512x512 generation...')
with urllib.request.urlopen(req, timeout=360) as res:
    data = json.loads(res.read().decode('utf-8'))
    imgs = data.get('images', [])
    print(f'Done in {time.time()-t0:.2f}s, images count: {len(imgs)}')
