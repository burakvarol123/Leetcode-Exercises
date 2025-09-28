var TimeLimitedCache = function() {
    this.store = new Map();
};

/** 
 * @param {number} key
 * @param {number} value
 * @param {number} duration time until expiration in ms
 * @return {boolean} if un-expired key already existed
 */
TimeLimitedCache.prototype.set = function(key, value, duration) {
    const now = Date.now();
    const prev = this.store.get(key);
    const existedAndAlive = prev && prev.expiresAt > now;

    this.store.set(key, {
        value: value,
        expiresAt: now + duration
    });

    return !!existedAndAlive;
};

/** 
 * @param {number} key
 * @return {number} value associated with key
 */
TimeLimitedCache.prototype.get = function(key) {
    const now = Date.now();
    const entry = this.store.get(key);
    if (!entry) return -1;

    if (entry.expiresAt <= now) {
        this.store.delete(key);
        return -1;
    }
    return entry.value;
};

/** 
 * @return {number} count of non-expired keys
 */
TimeLimitedCache.prototype.count = function() {
    const now = Date.now();
    for (const [key, entry] of this.store.entries()) {
        if (entry.expiresAt <= now) {
            this.store.delete(key);
        }
    }
    return this.store.size;
};

/**
 * const timeLimitedCache = new TimeLimitedCache()
 * timeLimitedCache.set(1, 42, 1000); // false
 * timeLimitedCache.get(1) // 42
 * timeLimitedCache.count() // 1
 */