#!/bin/bash
ssh_port='2001'
ssh -o StrictHostKeyChecking=no -R $ssh_port:localhost:22 srikant@10.101.30.28
