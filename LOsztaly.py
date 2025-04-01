# -*- coding: windows-1250 -*-
import redis
from redis import Redis

class LOsztaly():

    def __init__(self):
        redis_host = 'ip-address'
        redis_port = 6379

        self.r = Redis(host=redis_host, port=redis_port,
                       decode_responses=True)

    def game(self, week, serialnum, numbers):
        if self.r.exists('lsn_'+serialnum):
            raise Exception("Már volt ilyen sorozatszámú szelvény.")
        
        if len(numbers) != 5:
            raise Exception("Nem 5 számot választott!")
        for i in numbers:
            self.r.sadd('lsn_'+serialnum, i)

        self.r.sadd('w_'+week, 'lsn_'+serialnum)

    def list_week(self, week):
        for i in self.r.smembers('w_'+week):
            print(i)
            print(self.r.smembers(i))

    def numberOfPlayers(self, week):
        print(self.r.scard('w_'+week))

    def getNumber(self, serialnum):
        print(self.r.smembers('lsn_'+serialnum))

    def lottaryDrawn(self, week, numbers):
        
        for i in numbers:      
            self.r.sadd('w_'+week+'_drawn', i)

        for i in self.r.smembers('w_'+week):
            #print(i)
            #print('w_'+week+'_drawn')
            db = self.r.sintercard(2, ['w_'+week+'_drawn', i])
            print(db)
            if db!=0 and db!=1:
                self.r.sadd('w_'+week+'_winner_'+str(db), i)

    def winners(self, week, num):
        for i in self.r.smembers('w_'+week+'_winner_'+str(num)):
            print(i)

    def number_of_winners(self, week, num):
        print(self.r.scard('w_'+week+'_winner_'+str(num)))

